# Cuenta de Luz

Esta integración permite obtener las **tarifas eléctricas de Chile** desde [cuentadelaluz.cl](https://cuentadelaluz.cl/) y mostrarlas como **sensores** en Home Assistant según la comuna seleccionada.

## Características

- Selección de comuna en la configuración.
- Sensores para cada tipo de tarifa eléctrica.
- Actualización automática de los valores.

## Instalación en HACS

1. Agrega tu repositorio de GitHub como **Custom Repository** en HACS:
   - Tipo: `Integration`
   - URL: `https://github.com/tech178/cuenta_luz_ha`
2. Busca **Cuenta de Luz** en HACS → Integraciones → Instalar.
3. Reinicia Home Assistant.
4. Ve a **Configuración → Integraciones → Añadir Integración → Cuenta de Luz** y selecciona la comuna deseada.

## Uso

Después de configurar la integración:

- Cada tarifa aparecerá como un sensor independiente.
- Ejemplo de nombres de sensores:
  - `Cuenta Luz San Bernardo Cargo Fijo`
  - `Cuenta Luz San Bernardo Entre 200 y 210 kWh`
- Puedes usarlos en **automatizaciones, paneles y dashboards** como cualquier sensor de Home Assistant.

## Requisitos

- Home Assistant ≥ 2023.6
- Integración `requests` y `beautifulsoup4` (se instalan automáticamente vía `manifest.json`).

## Soporte

Si encuentras errores, revisa los **registros de Home Assistant** y abre un **issue en GitHub**.

