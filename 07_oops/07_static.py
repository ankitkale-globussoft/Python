# this is class:- 
class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def prntcar(self):
        print(f"{self.brand}, {self.model}")
    
    @staticmethod #this is a decorator used to make a method static
    def desc():
        print("Car is a mode of transport and amazing also")

# this is object:- 
myCar = Car('volkswagon', 'virtus')
Car.desc()