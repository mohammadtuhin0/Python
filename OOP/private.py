class Account:
    def __init__(self, account_no, acc_pass):
        self.account_no = account_no
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("251400052", "abcd")

print(acc1.account_no)
print(acc1.reset_pass)