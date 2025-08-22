# Cuenta de Luz - Home Assistant

Integración para consultar tarifas eléctricas por comuna desde cuentadelaluz.cl

## Instalación Manual
1. Copia `custom_components/cuenta_luz/` dentro de `config/custom_components/`
2. Reinicia Home Assistant
3. Ve a **Integraciones → Añadir integración → Cuenta de Luz**
4. Selecciona tu comuna

## HACS
Para usar esta integración desde HACS, crea un repo en GitHub con este contenido, agrega `hacs.json` y luego en HA:  
HACS → Integraciones → Repositorios personalizados → agrega tu repo → instala.

## Consideraciones
- El scraping actual es estático; hay que reemplazarlo por el scraping real que ya probaste.
- Las entidades se crean como `sensor.cuenta_luz_<comuna>_<tramo>`
