mark = int(input("Your marks : "))

if(mark >= 90):
    grade = "A"
elif(mark >=80 and mark< 90):
    grade = "B"
elif(mark >= 70 and mark < 80):
    grade = "C"
else:
    grade = "D"
    
print("Grade of the student -> ", grade)