"""
         Function Type-4 - 
Function With Parameter, With Return Value Type

4. Sum of all odd numbers between 1 to n

"""
# Function with parameter and return type
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):  #  odd numbers
        total += i
    return total

# Main program
n = int(input("Enter the value of n: "))

# Function calling 
result = sum_of_odds(n)

# print the result
print(f"Sum of all odd numbers from 1 to {n} = {result}")
