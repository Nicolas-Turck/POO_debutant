from cities import *
class City:
    def __init__(self, citizen):
        """method for initialise atrributs """
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.hydrate(citizen)

    def hydrate(self, citizen):
        """method for add elem in attribus"""
        for key_name, value_name in citizen.items():
            if hasattr(self, key_name):
                    setattr(self, key_name, value_name)
        
    def show_informations(self):
        """method for display elem of city"""
        identity_city = "card city \n \
        Name : {} \n\
        Department : {} \n\
        Country : {} \n\
        Population : {} \n\
        Mayor : {} \n"
        print(identity_city.format(self.name, self.department, self.country, self.population, sel