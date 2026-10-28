class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Withdrawal must be positive and within the balance.")
        self.balance -= amount


account = BankAccount("Ada", 20)
account.deposit(5)
account.withdraw(8)
print(f"{account.owner}'s balance: ${account.balance:.2f}")
