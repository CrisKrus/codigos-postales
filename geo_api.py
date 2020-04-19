import requests

from main import key

ID_PROVINCIA = 'CPRO'
ID_LAS_PALMAS = 35
CODIGO_POSTAL = 'CPOS'
ID_MUNICIPIO = 'CMUM'
NOMBRE_MUNICIPIO = 'DMUN50'
ID_POBLACION = 'CUN'
NOMBRE_POBLACION = 'NENTSI50'
ID_NUCLEO = 'CUN'
NOMBRE_NUCLEO = 'NNUCLE50'


def get_municipios(provincia_id):
    url = f"https://apiv1.geoapi.es/municipios?CPRO={provincia_id}&type=JSON&key={key}"
    res = requests.get(url)
    res = res.json()['data']

    municipios = []
    for municipio in res:
        municipios.append({'id': municipio[ID_MUNICIPIO], 'name': municipio[NOMBRE_MUNICIPIO]})
    return municipios


def get_poblacion(provincia_id, municipio_id):
    url = f"https://apiv1.geoapi.es/poblaciones?CPRO={provincia_id}&CMUM={municipio_id}&type=JSON&key={key}"
    res = requests.get(url)
    res = res.json()['data']

    poblaciones = []
    for poblacion in res:
        poblaciones.append({'id': poblacion[ID_POBLACION], 'name': poblacion[NOMBRE_POBLACION]})
    return poblaciones


def get_nucleo(provincia_id, municipio_id, poblacion_name):
    url = f"https://apiv1.geoapi.es/nucleos?CPRO={provincia_id}&CMUM={municipio_id}&NENTSI50={poblacion_name}&type=JSON&key={key}"
    res = requests.get(url)
    res = res.json()['data']

    nucleos = []
    for nucleo in res:
        nucleos.append({'id': nucleo[ID_NUCLEO], 'name': nucleo[NOMBRE_NUCLEO]})
    return nucleos


def get_codigo_postal(provincia_id, municipio_id, nucleo_id):
    url = f"https://apiv1.geoapi.es/cps?CPRO={provincia_id}&CMUM={municipio_id}&CUN={nucleo_id}&type=JSON&key={key}"
    res = requests.get(url)
    res = res.json()['data']

    codigos_postales = []
    for codigo_postal in res:
        codigos_postales.append(codigo_postal[CODIGO_POSTAL])
    return codigos_postales