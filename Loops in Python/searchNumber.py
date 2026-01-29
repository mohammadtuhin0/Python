tpl = (1,4,9,16,25,36,49, 64, 81, 100)

x = 25
i = 0
while i < len(tpl):
    if(tpl[i] == x):
        print("Found at index", i)
    else:
        print("Finding...")
    i+=1