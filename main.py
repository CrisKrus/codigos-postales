from sys import argv
from geo_api import geo_api


def write_all_postal_codes(infrastructura, id_provincia, nombre_provincia, output):
    municipios = infrastructura.get_municipios(id_provincia)

    for municipio in municipios:
        print(f"-> {municipio['name']}")
        poblaciones = infrastructura.get_poblacion(id_provincia, municipio['id'])

        for poblacion in poblaciones:
            print(f"\t-> {poblacion['name']}")
            nucleos = infrastructura.get_nucleo(id_provincia, municipio['id'], poblacion['name'])

            for nucleo in nucleos:
                print(f"\t\t-> {nucleo['name']}")
                codigos_postales = infrastructura.get_codigo_postal(id_provincia, municipio['id'], nucleo['id'])

                for codigo_postal in codigos_postales:
                    output.write(
                        f"{nombre_provincia}; {municipio['name']}; {poblacion['name']}; {nucleo['name']}; {codigo_postal};\n"
                    )


script, key, id_provincia = argv
file = None

try:
    geo = geo_api(key)
    nombre_provincia = geo.get_nombre_provincia(id_provincia)
    file = open(f'codigos_postales/{nombre_provincia}.csv', 'w')
    file.write('Provincia; Municipio; Poblacion; Nucleo; Codigo postal;\n')
    write_all_postal_codes(geo, id_provincia, nombre_provincia, file)
finally:
    file.close()
