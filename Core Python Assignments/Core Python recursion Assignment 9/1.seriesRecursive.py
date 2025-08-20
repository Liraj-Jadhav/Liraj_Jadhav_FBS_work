"""
# 1. Write a program to find sum of following series using recursive functions:

i. 1! + 2! + 3! + 4! +..... + n!

"""

# function to find factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1) # Recursive function Call

# Recursive function to find sum of series
def sumSeries(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sumSeries(n - 1) # Recursive function Call 


# Input from user
n = int(input("Enter the value of n: "))

# Output the result
print(f"Sum of series 1! + 2! + ... + {n}! = {sumSeries(n)}")
