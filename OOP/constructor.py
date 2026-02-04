# __init__ function --> Constructor

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")
    
s1 = Student("Tuhin", 89)
print(s1.name, s1.marks)

s2 = Student("Tasin", 98)
print(s2.name, s2.marks)