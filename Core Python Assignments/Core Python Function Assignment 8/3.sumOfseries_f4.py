
"""
        Function Type-4 - 
(Function With Parameter, With Return Value Type

3. Write a program to find sum of following series using functions :
a. 1+ 2 + 3 + 4+..... + n
b. 1!+ 2! + 3! + 4!+..... + n!
c. 1^1 + 2^2 + 3^3+ ...... n^n

"""
    
# Function for sum of natural numbers
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Function to calculate factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Function for sum of factorials
def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

# Function for sum of powers
def sum_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

# Main menu-driven program
while True:
    print("\nMenu:")
    print("1. Sum of series: 1 + 2 + 3 + ... + n")
    print("2. Sum of series: 1! + 2! + 3! + ... + n!")
    print("3. Sum of series: 1^1 + 2^2 + 3^3 + ... + n^n")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    """
    if choice == 4:
        print("Exiting program. Goodbye!")
        break
    """
    n = int(input("Enter the value of n: "))
    
    if choice == 1:
        print("Sum of natural numbers =", sum_natural(n))
    elif choice == 2:
        print("Sum of factorials =", sum_factorials(n))
    elif choice == 3:
        print("Sum of powers =", sum_powers(n))
    
    else:
        print("Invalid choice!, try again")

    # Break statement at the end (program stops after one operation)
#  break
