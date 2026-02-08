class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Tk.", amount, "was debited")
        print("total balance = ", self.get_balance())
        
    #credit
    def credit(self, amount):
        self.balance += amount
        print("TK.", amount, "was credited")
        print("total balance = ", self.get_balance())
        
        
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 251400052)
acc1.debit(1000)
acc1.credit(650)
acc1.credit(15000)
acc1.debit(3500)