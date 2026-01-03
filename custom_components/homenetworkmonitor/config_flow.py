"""Adds config flow for HomeNetworkMonitor."""

from __future__ import annotations

import logging

import voluptuous as vol
from homeassistant.const import (
    CONF_PASSWORD,
    CONF_URL,
    CONF_USERNAME,
)
from homeassistant.helpers import selector
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from slugify import slugify

from homeassistant import config_entries

from .api import (
    HomeNetworkMonitorApiClient,
    HomeNetworkMonitorApiClientAuthenticationError,
    HomeNetworkMonitorApiClientCommunicationError,
    HomeNetworkMonitorApiClientError,
)
from .const import DEFAULT_SCAN_INTERVAL, DOMAIN, LOGGER, UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)


class HomeNetworkMonitorFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for HomeNetworkMonitor."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}
        if user_input is not None:
            try:
                await self._test_credentials(
                    url=user_input[CONF_URL],
                    username=user_input[CONF_USERNAME],
                    password=user_input[CONF_PASSWORD],
                )
            except HomeNetworkMonitorApiClientAuthenticationError as exception:
                LOGGER.warning(exception)
                _errors["base"] = "auth"
            except HomeNetworkMonitorApiClientCommunicationError as exception:
                LOGGER.error(exception)
                _errors["base"] = "connection"
            except HomeNetworkMonitorApiClientError as exception:
                LOGGER.exception(exception)
                _errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(
                    ## Do NOT use this in production code
                    ## The unique_id should never be something that can change
                    ## https://developers.home-assistant.io/docs/config_entries_config_flow_handler#unique-ids
                    unique_id=slugify(user_input[CONF_USERNAME])
                )
                self._abort_if_unique_id_configured()
                # Add update_interval to the data
                user_input[UPDATE_INTERVAL] = user_input.get(UPDATE_INTERVAL, 5)
                return self.async_create_entry(
                    title=user_input[CONF_USERNAME],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_URL,
                        default=(user_input or {}).get(CONF_URL, ""),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.URL,
                        ),
                    ),
                    vol.Optional(
                        CONF_USERNAME,
                        default=(user_input or {}).get(CONF_USERNAME, ""),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.TEXT,
                        ),
                    ),
                    vol.Optional(CONF_PASSWORD, default=""): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.PASSWORD,
                        ),
                    ),
                    vol.Optional(
                        UPDATE_INTERVAL,
                        default=(user_input or {}).get(
                            UPDATE_INTERVAL, DEFAULT_SCAN_INTERVAL
                        ),
                    ): selector.NumberSelector(
                        selector.NumberSelectorConfig(
                            min=1,
                            max=60,
                            step=1,
                            unit_of_measurement="minutes",
                        ),
                    ),
                },
            ),
            errors=_errors,
        )

    async def async_step_reconfigure(
        self, user_input: dict | None = None
    ) -> config_entries.ConfigFlowResult:
        """Handle reconfiguration of the integration."""
        # Get the config entry from the context
        config_key = self.context.get("entry_id")
        if config_key is None:
            return self.async_abort(reason="missing_config_entry")

        config_entry = self.hass.config_entries.async_get_entry(config_key)
        if config_entry is None:
            return self.async_abort(reason="invalid_config_entry")
        self.config_entry = config_entry

        _errors = {}
        if user_input is not None:
            try:
                await self._test_credentials(
                    url=user_input[CONF_URL],
                    username=user_input[CONF_USERNAME],
                    password=user_input[CONF_PASSWORD],
                )
            except HomeNetworkMonitorApiClientAuthenticationError as exception:
                LOGGER.warning(exception)
                _errors["base"] = "auth"
            except HomeNetworkMonitorApiClientCommunicationError as exception:
                LOGGER.error(exception)
                _errors["base"] = "connection"
            except HomeNetworkMonitorApiClientError as exception:
                LOGGER.exception(exception)
                _errors["base"] = "unknown"
            else:
                # Update the config entry with new data
                updated_data = {**self.config_entry.data, **user_input}
                self.hass.config_entries.async_update_entry(
                    self.config_entry, data=updated_data
                )
                await self.hass.config_entries.async_reload(self.config_entry.entry_id)
                return self.async_abort(reason="reconfigure_successful")

        # Pre-fill the form with existing data
        return self.async_show_form(
            step_id="reconfigure",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_URL,
                        default=self.config_entry.data.get(CONF_URL, ""),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.URL,
                        ),
                    ),
                    vol.Optional(
                        CONF_USERNAME,
                        default=self.config_entry.data.get(CONF_USERNAME, ""),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.TEXT,
                        ),
                    ),
                    vol.Optional(CONF_PASSWORD, default=""): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.PASSWORD,
                        ),
                    ),
                    vol.Optional(
                        UPDATE_INTERVAL,
                        default=self.config_entry.data.get(UPDATE_INTERVAL, 5),
                    ): selector.NumberSelector(
                        selector.NumberSelectorConfig(
                            min=1,
                            max=60,
                            step=1,
                            unit_of_measurement="minutes",
                        ),
                    ),
                },
            ),
            errors=_errors,
        )

    async def _test_credentials(self, url: str, username: str, password: str) -> None:
        """Validate credentials."""
        client = HomeNetworkMonitorApiClient(
            url=url,
            username=username or "",
            password=password or "",
            session=async_create_clientsession(self.hass),
            hass=self.hass,
        )
        await client.async_get_data()
