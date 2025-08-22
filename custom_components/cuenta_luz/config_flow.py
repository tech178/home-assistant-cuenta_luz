from homeassistant import config_entries
from .const import DOMAIN
import voluptuous as vol
from homeassistant.helpers import config_validation as cv
from .test_cuenta_luz import obtener_tarifas

class CuentaLuzConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            comuna = user_input["comuna"]
            try:
                # validar que Selenium pueda obtener datos
                result = await self.hass.async_add_executor_job(obtener_tarifas, comuna)
                if "error" in result:
                    errors["base"] = "cannot_connect"
                else:
                    return self.async_create_entry(title=comuna, data={"comuna": comuna})
            except Exception:
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required("comuna"): str}),
            errors=errors,
        )
