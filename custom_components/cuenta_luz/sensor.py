from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    comuna = entry.data.get("comuna")
    opcion = entry.data.get("opcion")
    async_add_entities([CuentaLuzSensor(comuna, opcion)], True)

class CuentaLuzSensor(SensorEntity):
    def __init__(self, comuna, opcion):
        self._attr_name = f"Consumo Luz {comuna} ({opcion})"
        self._attr_unique_id = f"cuenta_luz_{comuna}_{opcion}".lower()
        self._state = None

    @property
    def native_value(self):
        return self._state

    async def async_update(self):
        # Aquí iría la lógica real de consulta web
        self._state = 123  # valor ficticio
