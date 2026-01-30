class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = "" ):
        self.ledger.append({"amount":amount, "description":description})
    
    def withdraw(self, amount, description=""):
        self.ledger.append({"amount": -amount, "description":description})
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance
    
    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {self.name}")
            destination.deposit(amount,f"Transfer from {self.name}" )
            return True

    def check_funds(self, amount):
        return amount <= self.get_balance()
    def __str__(self):
        print(self.name.center(30, "*"))
        for x in self.ledger:
            print()
    def create_spend_chart(categories):
        pass