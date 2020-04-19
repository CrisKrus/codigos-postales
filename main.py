from sys import argv
from geo_api import geo_api


def write_all_postal_codes(province_id, output):
    geo = geo_api(key)
    municipios = geo.get_municipios(province_id)

    for municipio in municipios:
        print(f"-> {municipio['name']}")
        poblaciones = geo.get_poblacion(province_id, municipio['id'])

        for poblacion in poblaciones:
            print(f"\t-> {poblacion['name']}")
            nucleos = geo.get_nucleo(province_id, municipio['id'], poblacion['name'])

            for nucleo in nucleos:
                print(f"\t\t-> {nucleo['name']}")
                codigos_postales = geo.get_codigo_postal(province_id, municipio['id'], nucleo['id'])

                for codigo_postal in codigos_postales:
                    output.write(
                        f"Las Palmas; {municipio['name']}; {poblacion['name']}; {nucleo['name']}; {codigo_postal};\n")


def chek(id_provincia):
    geo = geo_api(key)
    provincias = geo.get_provincias()

    contained = False
    for provincia in provincias:
        if provincia['id'] == id_provincia:
            contained = True

    if not contained:
        print('Codigo de provincia no valido')
        print('Provincias:')
        for provincia in provincias:
            print(provincia)
        exit(-1)


script, key, id_provincia = argv

chek(id_provincia)

file = open('codigos_postales/las_palmas.csv', 'w')

try:
    file.write('Provincia; Municipio; Poblacion; Nucleo; Codigo postal;\n')
    write_all_postal_codes(id_provincia, file)
finally:
    file.close()
