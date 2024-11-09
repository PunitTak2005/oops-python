class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self): 
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"


    def general_description(self):
        return 'Cars are means of transportation'

    def model_name(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, userbattery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = userbattery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", 120)
print(my_tesla.fuel_type())
print(my_tesla.general_description())

Car("Tata", "safari")
Car.model="city"
Car("Tata", "Nexon")

print(Car.total_car)

my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
