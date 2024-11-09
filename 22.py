class Car:

    def __init__(self,userbrand,usermodel):
        self.__brand = userbrand
        self.model = usermodel
    
    def get_brand(self):
        return self.__brand + "!"
    def full_name(self): 
        return f"{self.__brand}{self.model}"  
    
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self,userbrand, usermodel, userbattery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = userbattery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla","Model S", 120)
#print(my_tesla.__brand)
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.fuel_type())


# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name)

# my_new_car = Car("Tata","Safari")
# print(my_new_car.model)
