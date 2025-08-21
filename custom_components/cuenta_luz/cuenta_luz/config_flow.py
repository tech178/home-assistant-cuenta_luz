import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

OPCIONES = ["Base", "Punta", "Valle"]

class CuentaLuzConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        self.comuna = None
        self.opcion = "Base"

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            self.comuna = user_input["comuna"]
            self.opcion = user_input["opcion"]
            return self.async_create_entry(
                title=f"Costo Luz - {self.comuna}",
                data={
                    "comuna": self.comuna,
                    "opcion": self.opcion
                }
            )

        data_schema = vol.Schema({
            vol.Required("comuna"): str,
            vol.Required("opcion", default="Base"): vol.In(OPCIONES)
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema
        )
