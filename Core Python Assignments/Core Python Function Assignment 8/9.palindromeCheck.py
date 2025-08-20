"""
       Function Type-4 - 
Function With Parameter, With Return Value Type

9. Write a program to check if entered number is a palindrome or
not.

"""
# Function with parameter and return value
def isPalindrome(num):
    temp = num

    a = num % 10
    num = num // 10
    b = num % 10
    reverse = (a * 10) + b
    c = num // 10
    reverse = (reverse * 10) + c

    if temp == reverse:
        return True
    else:
        return False

# Main code
n = int(input("Enter a 3-digit number: "))
if isPalindrome(n):
    print(n, "is a palindrome number.")
else:
    print(n, "is not a palindrome number.")
