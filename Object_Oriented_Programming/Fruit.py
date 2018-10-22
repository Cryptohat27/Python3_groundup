class Fruit(object):
    def __init__(self):
        print("This is a fruit")

    def nutrition(self):
        print("We Like nutrition")

    def fruit_shape(self):
        print("Fruit has interesting shapes")

class Mango(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("Mangos are delicious")

    def nutrition(self):
        print("Mangos have good nutrition")

    def color(self):
        print("Mangos are orange and yellow")

F = Fruit()
F.nutrition()
F.fruit_shape()

O = Mango()
O.nutrition
O.color()
O.fruit_shape()
