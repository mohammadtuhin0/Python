# Write a recursive function to calculate the sum of first n natural numbers.

def calcu_sum(n):
    if(n == 0):
        return 0
    return calcu_sum(n - 1) + n
    
sum = calcu_sum(5)
print(sum)


# Write a recursive function to print all elements in a list. 

def prin_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    prin_list(list, idx+1)
    
fruits = ["mango", "litchi", "apple", "banana"]
prin_list(fruits)