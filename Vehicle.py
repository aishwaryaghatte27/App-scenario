class Vehicle:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display(self):
        for v in self.vehicles:
            print("Vehicle Number:", v.number)
            print("Brand:", v.brand)
            print("Price:", v.price)
            print("Category:", v.category())
            print()


s = Showroom()

v1 = Vehicle("MH12AB1234", "Toyota", 800000)
v2 = Vehicle("MH14CD5678", "BMW", 2500000)

s.add_vehicle(v1)
s.add_vehicle(v2)

s.display()
