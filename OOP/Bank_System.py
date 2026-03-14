class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdraw successful")
            
    def show_balance(self):
        print("Balance: ", self.balance)
        
acc = BankAccount("Tuhin", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.show_balance()