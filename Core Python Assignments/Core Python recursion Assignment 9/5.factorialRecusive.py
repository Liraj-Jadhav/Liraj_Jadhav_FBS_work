
# 5. Write a program to find factorial using recursion.


def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1) # this the recursive fuction call
    
n = int(input("Enter the Number n = "))

# Storing the return value and Calling the function 
x = factorial(n)

print(f"Factorial of {n} = {x}")