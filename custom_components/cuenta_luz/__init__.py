from .const import DOMAIN

async def async_setup_entry(hass, entry):
    """Configura la integración desde el flujo de configuración."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    return True

async def async_unload_entry(hass, entry):
    """Desinstala la integración al borrarla desde la UI."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
