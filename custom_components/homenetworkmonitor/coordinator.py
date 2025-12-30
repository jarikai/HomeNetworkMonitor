"""DataUpdateCoordinator for homenetworkmonitor."""

from __future__ import annotations

import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Any

from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import (
    HomeNetworkMonitorApiClient,
    HomeNetworkMonitorApiClientAuthenticationError,
    HomeNetworkMonitorApiClientError,
)
from .const import DOMAIN, UPDATE_INTERVAL

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import HomeNetworkMonitorConfigEntry

_LOGGER = logging.getLogger(__name__)


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class HomeNetworkMonitorDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: HomeNetworkMonitorConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        client: HomeNetworkMonitorApiClient,
        config_entry: HomeNetworkMonitorConfigEntry,
    ) -> None:
        """Initialize coordinator."""
        self.config_entry = config_entry
        self.client = client
        # Get update interval from config entry, default to 5 minutes
        update_interval = config_entry.data.get(UPDATE_INTERVAL, 5)

        # Convert minutes to timedelta
        update_interval_timedelta = timedelta(minutes=update_interval)

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=update_interval_timedelta,
            always_update=True,
        )

    async def _async_update_data(self) -> Any:
        """Update data via library."""
        try:
            data = await self.client.async_get_data()
            await self._async_process_raw(data)
            _LOGGER.debug("Data fetched successfully")
        except HomeNetworkMonitorApiClientAuthenticationError as exception:
            _LOGGER.exception("Authentication failed:")
            raise ConfigEntryAuthFailed(exception) from exception
        except HomeNetworkMonitorApiClientError as exception:
            _LOGGER.exception("API error occurred:")  # Changed from error to exception
            raise UpdateFailed(exception) from exception
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.exception(
                "Unexpected error:",
            )  # Changed from error to exception
            raise UpdateFailed(exception) from exception
        return data

    async def _async_process_raw(self, raw_data: Any) -> None:
        """Extract the ip of the host."""
        # raw_data comes from nmap: {"host": [...], "link": [...]}
        self._host_map = {self._extract_ip(h): h for h in raw_data.get("host", [])}
        _LOGGER.debug(
            "_host_map size %s in coordinator _async_process_raw", len(self._host_map)
        )

    @staticmethod
    def _extract_ip(host_data: dict) -> str:
        """Extract the ip of the host."""
        addr = host_data.get("address", [])
        if isinstance(addr, list) and addr:
            return addr[0].get("addr", "unknown")
        return host_data.get("ip", "unknown")

    @property
    def host_map(self) -> dict:
        """The available of the sensor ."""
        return self._host_map
