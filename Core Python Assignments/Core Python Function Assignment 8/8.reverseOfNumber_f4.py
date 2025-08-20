"""
      Function Type-4 - 
Function With Parameter, With Return Value Type

8. Write a program find reverse of a number

"""


# Function with parameter and return value
def reverseNumber(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse

# Main code
n = int(input("Enter a number: "))
result = reverseNumber(n)
print("Reverse of the number is:", result)
