from sys import argv

from geo_api import ID_LAS_PALMAS, get_municipios, get_poblacion, get_nucleo, get_codigo_postal

script, key, id_provincia = argv

with open('codigos_postales/las_palmas.csv', 'a') as file:
    file.write('Provincia; Municipio; Poblacion; Nucleo; Codigo postal;\n')
    municipios = get_municipios(ID_LAS_PALMAS)
    for municipio in municipios:
        print('--> ', municipio['name'])
        poblaciones = get_poblacion(ID_LAS_PALMAS, municipio['id'])
        for poblacion in poblaciones:
            print('----> ', poblacion['name'])
            nucleos = get_nucleo(ID_LAS_PALMAS, municipio['id'], poblacion['name'])
            for nucleo in nucleos:
                codigos_postales = get_codigo_postal(ID_LAS_PALMAS, municipio['id'], nucleo['id'])
                for codigo_postal in codigos_postales:
                        file.write(f"Las Palmas; {municipio['name']}; {poblacion['name']}; {nucleo['name']}; {codigo_postal};\n")
    file.close()
