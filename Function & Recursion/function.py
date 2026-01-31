a = 8
b = 2
sum = a + b
print(sum)

print("_______")
#function definition
def sum(a, b):
    s = a + b
    return s
print(sum(2, 3))    # function call

print("______")
# num = input("Enter 0 or 1 : ")
# if (num == 0):
#     def calSum(a, b):
#         sum = a + b
#         # return sum
#     print(calSum(5, 6))
# else:
#     def sumCal(x, y):
#         dec = x - y
#         return dec
#     print(sumCal(6, 5))
    
    
print("-------")

def print_hello():
    print("hello")

print_hello()

print("___________")
#average of 3 numbers
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(12, 8, 5)