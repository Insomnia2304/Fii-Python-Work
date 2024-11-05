class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, fuel_consumption):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption

    def mileage(self, miles):
        return miles / self.fuel_consumption

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, fuel_consumption):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption

    def mileage(self, miles):
        return miles / self.fuel_consumption
    
class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, fuel_consumption, towing_capacity):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.towing_capacity = towing_capacity

    def mileage(self, miles):
        return miles / self.fuel_consumption
    
    def get_towing_capacity(self):
        return self.towing_capacity
    
vehicles = [Car('Toyota', 'Corolla', 2015, 13, 30), Motorcycle('Honda', 'CBR', 2018, 8, 50), Truck('Ford', 'F-150', 2019, 23, 20, 10000)]
for vehicle in vehicles:
    print(vehicle.mileage(300))
    if isinstance(vehicle, Truck):
        print(vehicle.get_towing_capacity())
