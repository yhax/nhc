"""The NHC Integration component entry initializer."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)
DOMAIN = "nhc"
PLATFORMS = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up NHC from a UI config entry."""
    _LOGGER.info("Initializing UI-configured NHC Integration environment...")

    # Forward the setup task over to your sensor.py platform file automatically
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry if the user deletes it from the UI."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
➜  nhc cat config_flow.py 
"""Config flow for NHC integration."""
import logging
from homeassistant import config_entries
from homeassistant.core import callback

DOMAIN = "nhc"
_LOGGER = logging.getLogger(__name__)

class NHCConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for NHC Storm Tracker."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step when a user clicks 'Add Integration'."""
        # Prevent the user from adding your integration more than once
        if self._async_current_entries():
            return self.async_abort(reason="already_configured")

        if user_input is not None:
            # Create the integration entry with a friendly title
            return self.async_create_entry(title="NHC Storm Tracker", data={})

        # Display an empty submit form (no text boxes needed since it's fully automatic)
        return self.async_show_form(step_id="user")

