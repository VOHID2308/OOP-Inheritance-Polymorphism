class Employee:
    def calculate_bonus(self):
        pass

class Developer(Employee):
    def calculate_bonus(self):
        return "Bonus: 10% of salary"

class Manager(Employee):
    def calculate_bonus(self):
        return "Bonus: 20% of salary"

employees = [Developer(), Manager()]
for e in employees:
    print(e.calculate_bonus())