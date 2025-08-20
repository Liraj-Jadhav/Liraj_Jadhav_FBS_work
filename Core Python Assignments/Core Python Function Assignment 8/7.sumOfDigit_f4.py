"""
       Function Type-4 - 
Function With Parameter, With Return Value Type

7. Write a program to find sum of digits of a number.

"""
# Function with parameter and return type
def sumOfDigits(num):
    total = 0
    while num > 0:
        digit = num % 10        # get the last digit
        total += digit          # add it to total
        num = num // 10         # remove the last digit
    return total

# Main code
n = int(input("Enter a number: "))

# Function Calling and store the result
result = sumOfDigits(n)
print(f"Sum of digits of  the Number {n}: {result}")