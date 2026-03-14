class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
s1 = Student("Linus", 22)

del s1.age  

print("My name is",s1.name)  # This works
# print(s1.age) # This would cause an error