from sys import argv
from geo_api import geo_api
from postal_code import PostalCode


def get_all_postal_codes(infrastructura, id_provincia, nombre_provincia):
    postal_codes = []
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
                    postal_codes.append(PostalCode(nombre_provincia,
                                                   municipio['name'],
                                                   poblacion['name'],
                                                   nucleo['name'],
                                                   codigo_postal))
    return postal_codes


script, key, id_provincia = argv
file = None

try:
    geo = geo_api(key)
    nombre_provincia = geo.get_nombre_provincia(id_provincia)
    postal_codes = get_all_postal_codes(geo, id_provincia, nombre_provincia)

    file = open(f'codigos_postales/{nombre_provincia}.csv', 'w')
    csv_headers = PostalCode.get_csv_headers()
    file.write(f'{csv_headers}\n')

    for postal_code in postal_codes:
        postal_code_csv = postal_code.format_csv()
        file.write(f"{postal_code_csv}\n")

finally:
    file.close()
