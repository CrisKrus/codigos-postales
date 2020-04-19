import requests

ID_PROVINCIA = 'CPRO'
NOMBRE_PROVINCIA = 'PRO'

ID_MUNICIPIO = 'CMUM'
NOMBRE_MUNICIPIO = 'DMUN50'

ID_POBLACION = 'CUN'
NOMBRE_POBLACION = 'NENTSI50'

ID_NUCLEO = 'CUN'
NOMBRE_NUCLEO = 'NNUCLE50'

CODIGO_POSTAL = 'CPOS'


class geo_api:
    def __init__(self, key):
        self.KEY = key

    def get_municipios(self, provincia_id):
        url = f"https://apiv1.geoapi.es/municipios?CPRO={provincia_id}&type=JSON&key={self.KEY}"
        res = requests.get(url)
        res = res.json()['data']

        municipios = []
        for municipio in res:
            municipios.append({'id': municipio[ID_MUNICIPIO], 'name': municipio[NOMBRE_MUNICIPIO]})
        return municipios

    def get_poblacion(self, provincia_id, municipio_id):
        url = f"https://apiv1.geoapi.es/poblaciones?CPRO={provincia_id}&CMUM={municipio_id}&type=JSON&key={self.KEY}"
        res = requests.get(url)
        res = res.json()['data']

        poblaciones = []
        for poblacion in res:
            poblaciones.append({'id': poblacion[ID_POBLACION], 'name': poblacion[NOMBRE_POBLACION]})
        return poblaciones

    def get_nucleo(self, provincia_id, municipio_id, poblacion_name):
        url = f"https://apiv1.geoapi.es/nucleos?CPRO={provincia_id}&CMUM={municipio_id}&NENTSI50={poblacion_name}&type=JSON&key={self.KEY}"
        res = requests.get(url)
        res = res.json()['data']

        nucleos = []
        for nucleo in res:
            nucleos.append({'id': nucleo[ID_NUCLEO], 'name': nucleo[NOMBRE_NUCLEO]})
        return nucleos

    def get_codigo_postal(self, provincia_id, municipio_id, nucleo_id):
        url = f"https://apiv1.geoapi.es/cps?CPRO={provincia_id}&CMUM={municipio_id}&CUN={nucleo_id}&type=JSON&key={self.KEY}"
        res = requests.get(url)
        res = res.json()['data']

        codigos_postales = []
        for codigo_postal in res:
            codigos_postales.append(codigo_postal[CODIGO_POSTAL])
        return codigos_postales

    def get_provincias(self):
        url = f"https://apiv1.geoapi.es/provincias?&type=JSON&key={self.KEY}"
        res = requests.get(url)
        res = res.json()['data']

        provincias = []
        for provincia in res:
            provincias.append({
                'id': provincia[ID_PROVINCIA],
                'name': provincia[NOMBRE_PROVINCIA]
            })
        return provincias

    def chek_provincia(self, id_provincia):
        provincias = self.get_provincias()

        contenido = False
        for provincia in provincias:
            if provincia['id'] == id_provincia:
                contenido = True

        if not contenido:
            print('Codigo de provincia no valido')
            print('Provincias:')
            for provincia in provincias:
                print(provincia)
            exit(-1)

    def get_nombre_provincia(self, id_provincia):
        self.chek_provincia(id_provincia)

        provincias = self.get_provincias()
        for provincia in provincias:
            if id_provincia == provincia['id']:
                return provincia['name']
