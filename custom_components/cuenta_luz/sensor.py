from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .scraper import obtener_tarifas

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    comuna = entry.data["comuna"]
    tarifas_data = await hass.async_add_executor_job(obtener_tarifas, comuna)

    entities = []
    for key, value in tarifas_data["tarifas"].items():
        entities.append(TarifaSensor(comuna, key, value))
    async_add_entities(entities, True)

class TarifaSensor(SensorEntity):
    def __init__(self, comuna, key, value):
        self._attr_name = f"Cuenta Luz {comuna} {key}"
        self._attr_unique_id = f"cuenta_luz_{comuna}_{key}".replace(" ", "_").lower()
        self._attr_native_value = value
        self._attr_icon = "mdi:flash"

    @property
    def native_value(self):
        return self._attr_native_value

    async def async_update(self):
        # Actualizar datos
        tarifas_data = await self.hass.async_add_executor_job(
            obtener_tarifas, self._attr_name.split(" ")[2]
        )
        self._attr_native_value = tarifas_data["tarifas"].get(
            self._attr_name.split(" ", 3)[-1], self._attr_native_value
        )
