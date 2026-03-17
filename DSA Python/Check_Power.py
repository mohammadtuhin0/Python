def isPower(x, y):
    if x == 1:
        return y == 1
    
    result = 1
    while result < y:
        result *= x
        
    return result == y

if __name__ == '__main__':
    print(isPower(10, 1))
    print(isPower(1, 20))
    print(isPower(2, 128))