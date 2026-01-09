class Engine:
    def strat(self):
        print('Engine is ignited')

class Electric:
    def strat(self):
        print('this is electric engine')

class Car:
    def __init__(self, engine):
        self.engine = engine
    def drive(self):
        self.engine.strat()
        print('ready to drive')

car = Car(Electric())
car.drive()