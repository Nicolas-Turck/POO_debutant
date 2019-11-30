from class_city import *
from cities import *
#loops for registered elem in cities files 
for i  in cities:
    citizen = i
    citizen= City(citizen)
    print(citizen.__dict__)
    City.show_informations(citizen)