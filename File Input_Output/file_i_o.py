f = open("demo.txt", "r")
x = open("demo.txt", "a")

data = f.read()
print(data)
print(type(data))
f.close()

dt = x.write("\ni want to learn Python from ApnaCollege")