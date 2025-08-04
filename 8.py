class BankAccount:
    def get_interest(self):
        pass

class SavingsAccount(BankAccount):
    def get_interest(self):
        return "Interest rate: 5%"

class CheckingAccount(BankAccount):
    def get_interest(self):
        return "Interest rate: 1%"

accounts = [SavingsAccount(), CheckingAccount()]
for acc in accounts:
    print(acc.get_interest())