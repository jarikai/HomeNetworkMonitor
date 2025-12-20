"""NMap localnetwork API Client."""

from __future__ import annotations

import logging
import socket
from typing import TYPE_CHECKING, Any

import aiohttp
import async_timeout

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


class HomeNetworkMonitorApiClientError(Exception):
    """Exception to indicate a general API error."""


class HomeNetworkMonitorApiClientCommunicationError(
    HomeNetworkMonitorApiClientError,
):
    """Exception to indicate a communication error."""


class HomeNetworkMonitorApiClientAuthenticationError(
    HomeNetworkMonitorApiClientError,
):
    """Exception to indicate an authentication error."""


def _verify_response_or_raise(response: aiohttp.ClientResponse) -> None:
    """Verify that the response is valid."""
    if response.status in (401, 403):
        msg = "Invalid credentials"
        raise HomeNetworkMonitorApiClientAuthenticationError(
            msg,
        )
    response.raise_for_status()


class HomeNetworkMonitorApiClient:
    """NMap localnetwork API Client."""

    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        session: aiohttp.ClientSession,
        hass: HomeAssistant,
    ) -> None:
        """NMap localnetwork API Client."""
        self._url = url
        self._username = username
        self._password = password
        self._session = session
        self._hass = hass

    async def async_get_data(self) -> Any:
        """Get data from the API."""
        return await self._api_wrapper(
            method="get",
            url=self._url,
        )

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=data,
                )
                _verify_response_or_raise(response)
                return await response.json()

        except TimeoutError as exception:
            msg = f"Timeout error fetching information - {exception}"
            raise HomeNetworkMonitorApiClientCommunicationError(
                msg,
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            msg = f"Error fetching information - {exception}"
            raise HomeNetworkMonitorApiClientCommunicationError(
                msg,
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            msg = f"Something really wrong happened! - {exception}"
            raise HomeNetworkMonitorApiClientError(
                msg,
            ) from exception
