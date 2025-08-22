from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
import requests
from bs4 import BeautifulSoup

def obtener_tarifas(comuna: str):
    url = "https://cuentadelaluz.cl/"
    resp = requests.get(url, timeout=20)
    soup = BeautifulSoup(resp.text, "html.parser")
    select = soup.find("select", {"id": "comuna"})
    options = [opt.text.strip() for opt in select.find_all("option")]
    if comuna not in options:
        raise ValueError(f"Comuna '{comuna}' no encontrada")

    # Aquí deberás replicar la lógica POST o scraping del botón "Buscar"
    # Por ahora devolvemos un ejemplo estático (sustituir por tu lógica real)
    return {
        "Cargo Fijo": "$1.023,57",
        "Menos de 200 kWh": "$239,84",
        "Entre 200 y 210 kWh": "$240,99",
    }

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    comuna = entry.data["comuna"]
    data = obtener_tarifas(comuna)

    entities = [
        TarifaSensor(comuna, key, value)
        for key, value in data.items()
    ]
    async_add_entities(entities, True)

class TarifaSensor(SensorEntity):
    def __init__(self, comuna, key, value):
        self._attr_name = f"Cuenta Luz {comuna} {key}"
        self._attr_unique_id = f"cuenta_luz_{comuna}_{key}".replace(" ", "_").lower()
        self._attr_native_value = value
        self._attr_icon = "mdi:flash"

    @property
    def state(self):
        return self._attr_native_value
