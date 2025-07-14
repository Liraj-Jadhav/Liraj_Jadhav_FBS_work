# 7. Write a program to print first n prime numbers.

n = int(input("Enter first n prime  number you want : "))

count = 0     # Count for finding prime numbers 
num = 2       # Number to be checked for prime

print(" The First", n, "prime numbers are given below:")

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count = count + 1
    num += 1
