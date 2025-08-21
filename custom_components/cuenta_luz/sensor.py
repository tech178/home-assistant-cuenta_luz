import requests
from bs4 import BeautifulSoup
from homeassistant.helpers.entity import Entity
from datetime import timedelta

SCAN_INTERVAL = timedelta(minutes=30)

def setup_platform(hass, config, add_entities, discovery_info=None):
    pass  # Se usa solo el Config Flow

async def async_setup_entry(hass, entry, async_add_entities):
    comuna = entry.data["comuna"]
    opcion = entry.data["opcion"]
    async_add_entities([CuentaLuzSensor(comuna, opcion)], True)

class CuentaLuzSensor(Entity):
    def __init__(self, comuna, opcion):
        self._comuna = comuna
        self._opcion = opcion
        self._state = None
        self._unit_of_measurement = "CLP/kWh"

    @property
    def name(self):
        return f"Costo Luz - {self._comuna}"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    def update(self):
        try:
            url = f"https://cuentadelaluz.cl/{self._comuna}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            valor_tag = soup.find("span", {"id": f"valor-{self._opcion.lower()}"})
            if valor_tag:
                self._state = float(valor_tag.text.replace("CLP", "").strip())
            else:
                self._state = None
        except Exception as e:
            self._state = None
            print(f"Error al obtener el valor de luz: {e}")
