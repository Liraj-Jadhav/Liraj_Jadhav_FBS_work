
"""
8.a. Write a program to solve the following series :
a. 1! + 2! + 3! + 4! + .....n!

"""

# take input 
n = int(input("Enter the n: "))

fact_sum = 0

for i in range(1, n + 1):
    # Calculate factorial of i
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    # Add to sum
    fact_sum += fact

# Display result
print(f"Sum of the factorial series 1! + 2! + 3! + 4! + .....n! is: ",fact_sum)

