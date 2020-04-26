class PostalCode:
    def __init__(self, province, municipally, population, core, postal_code):
        self.postal_code = postal_code
        self.core = core
        self.population = population
        self.municipally = municipally
        self.province = province

    def format_csv(self):
        return "{}; {}; {}; {}; {};".format(
            self.province,
            self.municipally,
            self.population,
            self.core,
            self.postal_code
        )

    @classmethod
    def get_csv_headers(cls):
        return 'Provincia; Municipio; Poblacion; Nucleo; Codigo postal;'
