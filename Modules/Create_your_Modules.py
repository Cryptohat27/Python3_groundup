"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
#import car as car
from Modules import car 
class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        car.info(make, model)
m = ModulesDemo()
m.builtin_modules()
m.car_description()
