class Vehicle:
    def show_info(self):
        pass

class Car(Vehicle):
    def show_info(self):
        return "Car: 4 wheels, comfortable seats"

class Bike(Vehicle):
    def show_info(self):
        return "Bike: 2 wheels, lightweight"

vehicles = [Car(), Bike()]
for v in vehicles:
    print(v.show_info())