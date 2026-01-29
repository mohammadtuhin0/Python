# # Break 
# i = 1
# while i <=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("End loop")



tpl = (1,4,9,16,25,36,49, 64, 81, 100)

x = 25
i = 0
while i < len(tpl):
    if(tpl[i] == x):
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i+=1
    
# Continue 
y = 0
while y <= 5:
    if(y == 3):
        y += 1
        continue
    print(y)
    y += 1