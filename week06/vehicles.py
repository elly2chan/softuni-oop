from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_consumtpion = self.fuel_consumption * distance + distance * 0.9
        if self.fuel_quantity >= fuel_consumtpion:
            self.fuel_quantity -= fuel_consumtpion

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_consumtpion = self.fuel_consumption * distance + distance * 1.6
        if self.fuel_quantity >= fuel_consumtpion:
            self.fuel_quantity -= fuel_consumtpion

    def refuel(self, fuel):
        given_fuel = fuel - (fuel * 0.05)
        self.fuel_quantity += given_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)