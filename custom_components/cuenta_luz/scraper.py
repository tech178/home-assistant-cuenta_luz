import requests
from bs4 import BeautifulSoup

def obtener_tarifas(comuna: str):
    url = "https://cuentadelaluz.cl/"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Validar comuna
    select = soup.find("select", {"id": "comuna"})
    opciones = [opt.text.strip() for opt in select.find_all("option")]
    if comuna not in opciones:
        raise ValueError(f"Comuna '{comuna}' no encontrada")

    # Simular seleccionar la comuna y presionar buscar
    # Aquí se hace scraping simple, por si la página devuelve todo
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

    return {"comuna": comuna, "tarifas": tarifas}
