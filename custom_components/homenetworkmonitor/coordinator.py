"""DataUpdateCoordinator for homenetworkmonitor."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import (
    HomeNetworkMonitorApiClientAuthenticationError,
    HomeNetworkMonitorApiClientError,
)

if TYPE_CHECKING:
    from .data import HomeNetworkMonitorConfigEntry

_LOGGER = logging.getLogger(__name__)


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class HomeNetworkMonitorDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: HomeNetworkMonitorConfigEntry

    async def _async_update_data(self) -> Any:
        """Update data via library."""
        try:
            data = await self.config_entry.runtime_data.client.async_get_data()
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
