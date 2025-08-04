"""Config flow for solax integration."""

from __future__ import annotations

import logging
from typing import Any

from solax import real_time_api
from solax.discovery import DiscoveryError
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD, CONF_PORT
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

DEFAULT_IP = "192.168.1.36"
DEFAULT_PORT = 80
DEFAULT_PASSWORD = "admin"
#DEFAULT_INVERTER_TYPE = "x1_boost"

#CONF_INVERTER_TYPE = "inverter_type"  # this should be from homeassistant.const, but it's not defined there

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP_ADDRESS, default=DEFAULT_IP): cv.string,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
        vol.Optional(CONF_PASSWORD, default=DEFAULT_PASSWORD): cv.string,
        # This is a placeholder for future expansion
        # as the solax library supports more inverter types
        # and the dropdown will be populated with the available types
        # and the user can select one of them
        # For now, we will just use "x1_boost"
        # vol.Required(CONF_INVERTER_TYPE, default=DEFAULT_INVERTER_TYPE): vol.In(
        #    [
        #        "x1_boost",
        #    ]
        #),
    }
)


async def validate_api(data) -> str:
    """Validate the credentials."""

    api = await real_time_api(
        data[CONF_IP_ADDRESS], data[CONF_PORT], data[CONF_PASSWORD]
    )
    response = await api.get_data()
    return response.serial_number


class SolaxConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Solax."""

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, Any] = {}
        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
            )

        try:
            serial_number = await validate_api(user_input)
        except (ConnectionError, DiscoveryError):
            errors["base"] = "cannot_connect"
        except Exception:
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            await self.async_set_unique_id(serial_number)
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=serial_number, data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )
