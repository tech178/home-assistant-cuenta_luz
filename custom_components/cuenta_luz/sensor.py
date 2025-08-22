from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

def obtener_tarifas(comuna):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://cuentadelaluz.cl/")
        select = Select(driver.find_element(By.ID, "comuna"))
        select.select_by_visible_text(comuna)
        boton = driver.find_element(By.ID, "buttonSearch")
        boton.click()
        time.sleep(3)

        filas = driver.find_elements(By.CSS_SELECTOR, "div.info-row")
        tarifas = {}
        for fila in filas:
            try:
                clave = fila.find_element(By.TAG_NAME, "strong").text.strip(":")
                valor = fila.find_element(By.TAG_NAME, "span").text
                if "Porcentaje" in clave or "%" in clave:
                    continue
                tarifas[clave] = valor
            except:
                continue
        return tarifas
    finally:
        driver.quit()


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
        clave = self._attr_name.split(" ", 3)[-1]
        self._attr_native_value = data.get(clave, self._attr_native_value)
