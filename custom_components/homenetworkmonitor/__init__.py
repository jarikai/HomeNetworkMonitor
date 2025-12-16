"""
Custom integration to integrate NMap data with Home Assistant homenetworkmonitor.

For more details about this integration, please refer to
https://github.com/jarikai/homenetworkmonitor
"""

from __future__ import annotations

import logging
from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.const import CONF_PASSWORD, CONF_URL, CONF_USERNAME, Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.loader import async_get_loaded_integration

from .api import HomeNetworkMonitorApiClient
from .const import DOMAIN, LOGGER
from .coordinator import HomeNetworkMonitorDataUpdateCoordinator
from .data import HomeNetworkMonitorData

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import HomeNetworkMonitorConfigEntry

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
]

_LOGGER = logging.getLogger(__name__)


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(
    hass: HomeAssistant,
    entry: HomeNetworkMonitorConfigEntry,
) -> bool:
    """Set up this integration using UI."""
    coordinator = HomeNetworkMonitorDataUpdateCoordinator(
        hass=hass,
        logger=LOGGER,
        name=DOMAIN,
        update_interval=timedelta(minutes=5),
    )
    # Store data for this config entry
    entry.runtime_data = HomeNetworkMonitorData(
        client=HomeNetworkMonitorApiClient(
            url=entry.data[CONF_URL],
            username=entry.data[CONF_USERNAME],
            password=entry.data[CONF_PASSWORD],
            session=async_get_clientsession(hass),
        ),
        integration=async_get_loaded_integration(hass, entry.domain),
        coordinator=coordinator,
    )

    # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
    await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: HomeNetworkMonitorConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(
    hass: HomeAssistant,
    entry: HomeNetworkMonitorConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
