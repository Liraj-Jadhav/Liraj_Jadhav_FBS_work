# 1. Factors of a given number

# Function definition
def Factors(num):
    print(f"Factors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

# Function Call and store return value
number = int(input("Enter a number: "))
Factors(number)