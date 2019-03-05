#Mark Johnston

numba_one = int(input("Enter one number: "))
while numba_one <0:
    print("Invalid entry, number must be positive")
    numba_one = int(input("Enter one number: "))
    
numba_two = int(input("Enter second number: "))
while numba_two <0:
    print("Invalid entry, number must be positive")
    numba_two = int(input("Enter second number: "))
    

print(numba_one + numba_two)
print(numba_one - numba_two)
