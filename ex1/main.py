from class_city  import *
#ask function main in class_city.py for launch program
#instancie attributs
city = City("Mont-Saint-Aignan", 76)
city1 = City("Lille", 59)
city2 = City("Paris", 75)
city3 = City("Lyon", 69)
city4 = City("Marseille",  13)
city5 = City("Bordeaux", 30)


   
City.show_location(city)
City.show_location(city1)
City.show_location(city2)
City.show_location(city3)
City.show_location(city4)
City.show_location(city5)
#ask function for change name and department
City.change_location(city3)
#display items of city3 change 
print(city3.__dict__)
    