class Car:

    def __init__(self,userbrand,usermodel):
        self.brand = userbrand
        self.model = usermodel
    def full_name(self): 
        return f"{self.brand}{self.model}"  

class ElectricCar(Car):
    def __init__(self,userbrand, usermodel, userbattery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = userbattery_size

my_tesla = ElectricCar("Tesla","Model S", 120)
print(my_tesla.full_name)


my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name)

my_new_car = Car("Tata","Safari")
print(my_new_car.model)
