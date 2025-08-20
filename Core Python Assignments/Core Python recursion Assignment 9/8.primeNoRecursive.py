
# 8. Write a program to check whether a number is prime or not using recursion.

def checkPrime(num, i=2):
    if num <= 1:
        return False
    if i == num:   # checked all numbers till n-1
        return True
    if num % i == 0:
        return False
    return checkPrime(num, i + 1)

# take input from user
num = int(input("Enter the number: "))

if checkPrime(num):
    print(num, "is the Prime number")
else:
    print(num, "is Not a Prime number")
