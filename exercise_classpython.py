class Account:
    def __init__(self, account_name, account_number, balance = 0):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_name} deposited {amount}. Now the balance is {self.balance}")
        else:
            print("Deposit amount must be positive.")
            
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_name, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            new_account=Account(account_name, account_number, initial_balance)
            print(f"Account number: {new_account.account_number} created for {new_account.account_name}")
            self.accounts[account_number] = new_account
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None
account1 = Account("Alice", "123456789", 1000)
account1.deposit(500)
bank_of_america = Bank()
bank_of_america.create_account(account1.account_name, account1.account_number, account1.balance)
account = bank_of_america.get_account("123456789")

print("Bank of America Accounts:")
for acc in bank_of_america.accounts.values():
    print(f"Account Name: {acc.account_name}, Account Number: {acc.account_number}, Balance: ${acc.balance}")
if account:
    print(f"Account Name: {account.account_name}, Account Number: {account.account_number}, Balance: ${account.balance}")