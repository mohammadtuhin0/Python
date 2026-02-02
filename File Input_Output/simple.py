# import os

# os.remove("simple.txt")


# with open("practice.txt", "w") as f:
#     f.write("HI everyone!\nwe are lerning File I\O\n")
#     f.write("using Java.\nI like Programming in Java.")
    

# with open("practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("Java", "Python")
# print(new_data)


# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")


def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
    if(word in data):
        print("Found")
    else:
        print("Not Found")
        
check_for_word()


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()