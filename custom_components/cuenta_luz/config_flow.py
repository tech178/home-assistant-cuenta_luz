from homeassistant import config_entries
from .const import DOMAIN
import requests
from bs4 import BeautifulSoup

class CuentaLuzConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    def __init__(self):
        self.comuna = None

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            comuna = user_input["comuna"]
            try:
                # Validar que la comuna existe
                opciones = await self.hass.async_add_executor_job(self.obtener_comunas)
                if comuna not in opciones:
                    errors["comuna"] = "invalid_comuna"
                else:
                    self.comuna = comuna
                    return self.async_create_entry(title=comuna, data={"comuna": comuna})
            except Exception:
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=self._build_schema(),
            errors=errors,
        )

    def _build_schema(self):
        import voluptuous as vol
        from homeassistant.helpers import config_validation as cv
        return vol.Schema({
            vol.Required("comuna"): str
        })

    def obtener_comunas(self):
        url = "https://cuentadelaluz.cl/"
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        select = soup.find("select", {"id": "comuna"})
        return [opt.text.strip() for opt in select.find_all("option")]
