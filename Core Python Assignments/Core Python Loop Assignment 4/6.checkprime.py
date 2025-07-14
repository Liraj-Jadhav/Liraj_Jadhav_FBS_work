# 6. WAP to check if a given number is prime number or not.

# take input from user
num = int(input("Enter the number: "))

for i in range(2,num):
    if(num % i ==0):
        print(num," ia Not a Prime number")
        break
else:
    print(num," is the Prime number")

