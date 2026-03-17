def isPrime(n):
    if n <= 1:
        return False
    
    # check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True


# Drive program to test above function 
print("true") if isPrime(11) else print("false")
print("true") if isPrime(14) else print("false")