class Car:
    @staticmethod
    def start():
        print("Car started...")
        
    @staticmethod
    def stop():
        print("Car stoped...")
        
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        
car1 = Fortuner("diesel")
car1.start()
        
# car1 = ToyotaCar("Fartuner")
# car2 = ToyotaCar("Prius")

# print(car1.start())