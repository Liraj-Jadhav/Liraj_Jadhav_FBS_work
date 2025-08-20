"""
         Function Type-4 - 
Function With Parameter, With Return Value Type

5. Sum of all prime numbers between 1 to n

"""
## Function with parameter and return type to find sum of prime numbers
def sumOfPrimes(n):
    total = 0
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):  # simple loop from 2 to num-1
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total += num
    return total

# Input from user
n = int(input("Enter the value of n: "))

# Call the function and display result
result = sumOfPrimes(n)
print(f"Sum of all prime numbers from 1 to {n} is {result}")
