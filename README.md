Codigos postales
================

Con este repositorio puedes obetener todos los códigos postales de una provincia de España concreta. Se está haciendo
uso de una API abierta [GeoAPI España](https://geoapi.es/inicio).

Arrancar al proyecto
--------------------

Versión de Python: __3.6.10__

1. Clonar/descargar el proyecto
2. instalar dependencias `pip install --no-cache-dir -r requirements.txt`
3. obtener clave para poder usar la API. Tienes que registrarte y te dejara una API key para poder hacer uso de ella
4. lanzar el programa `python main.py <API key> <codigo provincia>`
    - Sustituir `<API key>` y `<codigo provincia>` por los valores que quieras. Por ejemplo 35 es la provincia de Las 
    Palmas
5. Una vez el proceso termina en el directorio `codigos_postales` estará el resultado en formato `csv`

Todo list
---------

- [ ] Poner lista de provincias en el README
- [ ] Generalizar mas a comunidades (?)
- [ ] Dockerfile
- [ ] Añadir modulo que separe por islas
- [ ] Problemas de encoding