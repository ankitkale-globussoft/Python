# here we will see how to find out is a object instance or inheritance of a class or not

# this is class:- 
class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def prntcar(self):
        print(f"{self.brand}, {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # Method Override 
    def prntcar(self):
        super().prntcar()
        print(self.battery_size)

elc = ElectricCar('Tesla', 'X', '450kwh')

print(isinstance(elc, ElectricCar))
print(isinstance(elc, Car))