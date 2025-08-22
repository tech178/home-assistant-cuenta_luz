from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .test_cuenta_luz import obtener_tarifas  # tu código de Selenium o requests/BS4

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    comuna = entry.data["comuna"]
    data = obtener_tarifas(comuna)

    entities = [TarifaSensor(comuna, key, value) for key, value in data.items()]
    async_add_entities(entities, True)

class TarifaSensor(SensorEntity):
    def __init__(self, comuna, key, value):
        self._comuna = comuna
        self._key = key
        self._attr_name = f"Cuenta Luz {comuna} {key}"
        self._attr_unique_id = f"cuenta_luz_{comuna}_{key}".replace(" ", "_").lower()
        self._attr_native_value = value
        self._attr_icon = "mdi:flash"

    async def async_update(self):
        data = obtener_tarifas(self._comuna)
        self._attr_native_value = data.get(self._key, self._attr_native_value)
