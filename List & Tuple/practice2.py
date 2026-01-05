# list1 = [1, 2, 1,]
list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("not palindrome")
    

# count 
grade = ["C", "D", "A", "A", "B", "B", "A"]
# print(grade.count("A"))
grade.sort()
print(grade)