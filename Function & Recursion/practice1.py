# WAF to print the length of a list. (list is the parameter)

cities = ["dhaka", "gazipur", "rongpur", "rajsahi", "borishal"]
heros = ["thor", "ironman", "spriderman", "captain america"]

def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heros)


# WAF to print the elements of a list in a single line.

def print_list(list):
    for item in list:
        print(item, end=" ")
        
print_list(heros)
print_list(cities)


#WAF to find the factorial of n.
print("\nFactorial :")
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
calc_fact(6)


#WAF to convert USD to BDT:

def converter(usd_val):
    bdt_val = usd_val * 120
    print(usd_val, "USD =", bdt_val, "BDT")

converter(2)