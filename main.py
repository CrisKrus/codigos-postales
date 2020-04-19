from sys import argv
from geo_api import geo_api


def write_all_postal_codes(province_id, province_name, output):
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
                        f"{province_name}; {municipio['name']}; {poblacion['name']}; {nucleo['name']}; {codigo_postal};\n"
                    )


script, key, id_provincia = argv
file = None

try:
    geo = geo_api(key)
    province_name = geo.get_nombre_provincia(id_provincia)
    file = open(f'codigos_postales/{province_name}.csv', 'w')
    file.write('Provincia; Municipio; Poblacion; Nucleo; Codigo postal;\n')
    write_all_postal_codes(id_provincia, province_name, file)
finally:
    file.close()
