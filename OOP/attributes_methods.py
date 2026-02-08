class Student:
    college_name = "ABC College"
    name = "anonymous" # class attr
    
    def __init__(self, name, marks):
        self.name = name #Obj attr > class attr
        self.marks = marks
        
    def welcome(self):
        print("welocme student")
        
    def get_marks(self):
        return self.marks
        
s1 = Student("Tasin", 97)
print(s1.name)
print(s1.get_marks())