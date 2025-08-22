# Cuenta de Luz - Home Assistant Integration

Esta integración permite consultar las tarifas de electricidad de [cuentadelaluz.cl](https://cuentadelaluz.cl/) directamente desde Home Assistant. Los valores se muestran como **sensores** y se actualizan al refrescar la integración.

## Funcionalidades

- Selección de comuna durante la instalación.
- Cada tarifa aparece como un sensor individual en Home Assistant.
- Actualización automática de los valores de tarifa.

## Requisitos

- Home Assistant 2023.10 o superior.
- Selenium y WebDriver Manager para Python (instalados automáticamente desde `manifest.json`).

## Instalación vía HACS

1. Agregar este repositorio en HACS: `https://github.com/tech178/cuenta_luz_ha`
2. Instalar la integración desde HACS.
3. Reiniciar Home Assistant.
4. Agregar la integración desde **Configuración → Dispositivos y Servicios → Agregar Integración**.
5. Seleccionar la comuna deseada y confirmar.

## Uso

Una vez agregada, cada tarifa será un sensor:

- `sensor.cuenta_luz_san_bernardo_menos_de_200_kwh`
- `sensor.cuenta_luz_san_bernardo_entre_200_y_210_kwh`
- ...

## Notas

- Utiliza Selenium en modo `headless`, no requiere abrir navegador visible.
- La integración puede tardar unos segundos en obtener los datos dependiendo de la comuna seleccionada.

## Autor

[@tech178](https://github.com/tech178)


