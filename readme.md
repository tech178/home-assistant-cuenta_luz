# Cuenta de Luz

Integración de Home Assistant para obtener tarifas eléctricas de [cuentadelaluz.cl](https://cuentadelaluz.cl).

## Instalación

1. Copiar la carpeta `cuenta_luz` a `custom_components` de Home Assistant.
2. Reiniciar Home Assistant.
3. Agregar la integración desde **Configuración → Dispositivos e Integraciones**.
4. Seleccionar la comuna deseada.

## Funcionalidad

- Cada tarifa eléctrica se crea como un sensor independiente.
- Actualiza los valores al presionar el botón "Actualizar" en la integración.
- Compatible con HACS.

## Requisitos

- `requests`
- `beautifulsoup4`


