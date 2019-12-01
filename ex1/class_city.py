class City:
    
    def __init__(self, name, department):
        """method for initialise atrributs """
        self.name = name
        self.department = department

    def show_location(self):
        """this method return the city and the department"""
        print(" the city {} is in the department {}".format(self.name, self.department))
    
    def change_location(self):
        """method for change location of city"""
        print(" the city to change name is {} and the department is {}".format(self.name, self.department))
        #change value of name and department for entry user 
        self.name = input("enter a city :")
        self.department = int(input("enter the department :"))
        print("new city is {} and the department is {}".format(self.name, self.department))
        #display for verify the new items for name and department