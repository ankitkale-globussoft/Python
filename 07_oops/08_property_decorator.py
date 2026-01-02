# this is class:- 
class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    def prntcar(self):
        print(f"{self.brand}, {self.__model}")

    @property
    def model(self):
        return self.__model
    
    @staticmethod #this is a decorator used to make a method static
    def desc():
        print("Car is a mode of transport and amazing also")

# this is object:- 
myCar = Car('volkswagon', 'virtus')
Car.desc()

# Now lets make a property decorator so that model can be assigned only once and after it should be readonly

print(myCar.brand)