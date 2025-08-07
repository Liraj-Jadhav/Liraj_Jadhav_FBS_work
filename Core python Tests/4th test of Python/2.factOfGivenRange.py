# Factorial of All numbers in a given Range

# Recursive function 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # recursive Function Call

# take range input
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print(f"Factorials from {start} to {end} are:")
for i in range(start, end + 1):
    print(f"{i}! = {factorial(i)}")
