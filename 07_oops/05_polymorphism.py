# this is class:- 
class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def prntcar(self):
        print(f"{self.brand}, {self.model}")
    def fuel_type(self):
        print('runs on petrol')

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # Method Override 
    def prntcar(self):
        super().prntcar()
        print(self.battery_size)
    
    def fuel_type(self):
        print('runs on electricity')

myTesla = ElectricCar('Tesla', 'X', '450kwh')
myTesla.prntcar()
myTesla.fuel_type()

mySafari = Car('Tata', 'Safari')
mySafari.prntcar()
mySafari.fuel_type()

# class k andr k mehtod me self as a first arg dena jaruri hai