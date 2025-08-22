from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
import requests
from bs4 import BeautifulSoup

def obtener_tarifas(comuna):
    url = "https://cuentadelaluz.cl/"
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")

    # Seleccionar la comuna y simular click en "Buscar"
    select = soup.find("select", {"id": "comuna"})
    opciones = [opt.text.strip() for opt in select.find_all("option")]
    if comuna not in opciones:
        raise ValueError(f"Comuna '{comuna}' no encontrada")

    # Extraer los resultados de la tabla
    filas = soup.select("div.info-row")
    tarifas = {}
    for fila in filas:
        try:
            clave = fila.find("strong").text.strip(":")
            valor = fila.find("span").text
            if "Porcentaje" in clave or "%" in clave:
                continue
            tarifas[clave] = valor
        except:
            continue

    return tarifas


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    comuna = entry.data["comuna"]
    data = await hass.async_add_executor_job(obtener_tarifas, comuna)

    entities = [TarifaSensor(comuna, key, value) for key, value in data.items()]
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
        comuna = self._attr_name.split(" ")[2]
        data = await self.hass.async_add_executor_job(obtener_tarifas, comuna)
        key = " ".join(self._attr_name.split(" ")[3:])
        self._attr_native_value = data.get(key, self._attr_native_value)

