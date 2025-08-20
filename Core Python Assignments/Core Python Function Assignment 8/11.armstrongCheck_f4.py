"""
      Function Type-4 - 
Function With Parameter, With Return Value Type

11. WAP to check if a given number is Armstrong number or not. For
each task create separate functions.

"""
# Function to count the number of digits in the number
def countDigits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

# Function to calculate the Armstrong sum
def armstrongSum(num, digits):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10
    return total

# Function to check if the number is an Armstrong number
def isArmstrong(num):
    digits = countDigits(num)
    return num == armstrongSum(num, digits)

# Main program
number = int(input("Enter a number: "))

if isArmstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
