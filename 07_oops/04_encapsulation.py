class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self): # getter method
        print(self.__brand)
    
    def set_brand(self, brand): # setter method
        self.__brand = brand

    def prntcar(self):
        print(f"{self.__brand}, {self.model}")

elc = Car('Tesla', 'X')
elc.get_brand()
elc.set_brand('! Tesla')
elc.get_brand()