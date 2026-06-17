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

