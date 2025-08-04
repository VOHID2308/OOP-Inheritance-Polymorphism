class Appliance:
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class TV(Appliance):
    def turn_on(self):
        return "TV turned on"
    def turn_off(self):
        return "TV turned off"

class Fridge(Appliance):
    def turn_on(self):
        return "Fridge started cooling"
    def turn_off(self):
        return "Fridge stopped cooling"

appliances = [TV(), Fridge()]
for a in appliances:
    print(a.turn_on())
    print(a.turn_off())