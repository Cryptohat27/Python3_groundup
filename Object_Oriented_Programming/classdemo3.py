"""
Object Oriented Programming
"""

class Car(object):

    Wheels = 4
    

    def __init__(self, make, model):
        self.make = make
        self.model = model
    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model) 

print(Car.Wheels)
c1 = Car('bmw', '550i')
c1.Wheels = 3
print(c1.Wheels)
c1.info()

c2 = Car('benz', 'E350')
print(c2.make)
print(c2.Wheels)
c2.info()


