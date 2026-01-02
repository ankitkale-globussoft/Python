# this is class:- 

class Car():
    count = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.count += 1
    def prntcar(self):
        print(f"{self.brand}, {self.model}")

# this is object:- 
Car('volkswagon', 'virtus')
Car('volkswagon', 'virtus')
Car('volkswagon', 'virtus')
Car('volkswagon', 'virtus')
print(Car.count)    