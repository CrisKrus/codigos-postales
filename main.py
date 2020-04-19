from sys import argv
from geo_api import geo_api

script, key, id_provincia = argv

geo = geo_api(key)

file = open('codigos_postales/las_palmas.csv', 'w')

try:
    file.write('Provincia; Municipio; Poblacion; Nucleo; Codigo postal;\n')
    municipios = geo.get_municipios(id_provincia)

    for municipio in municipios:
        print(f"-> {municipio['name']}")
        poblaciones = geo.get_poblacion(id_provincia, municipio['id'])

        for poblacion in poblaciones:
            print(f"\t-> {poblacion['name']}")
            nucleos = geo.get_nucleo(id_provincia, municipio['id'], poblacion['name'])

            for nucleo in nucleos:
                print(f"\t\t-> {nucleo['name']}")
                codigos_postales = geo.get_codigo_postal(id_provincia, municipio['id'], nucleo['id'])

                for codigo_postal in codigos_postales:
                    file.write(
                        f"Las Palmas; {municipio['name']}; {poblacion['name']}; {nucleo['name']}; {codigo_postal};\n")
finally:
    file.close()