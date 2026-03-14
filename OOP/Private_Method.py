class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass      # password private
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("252400052", "eu123")

print("This is my Account No : ",acc1.acc_no)
# print("This is my Account Password : ", acc1.__acc_pass)

print(acc1.reset_pass())