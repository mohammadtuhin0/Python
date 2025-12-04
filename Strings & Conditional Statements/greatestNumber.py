a = int(input("enter first number : "))
b = int(input("enter second number :"))
c = int(input("enter third number : "))

if(a>b and a>c):
    print("first number largest" ,a)
elif(b>a and b>c):
    print("second number largest", b)
else:
    print("third number largest", c)