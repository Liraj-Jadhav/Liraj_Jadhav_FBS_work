
# 4. Write a program to find sum of n numbers using recursion.

def recursiveSum(n):
    if n == 0:
        return 0
    else:
        return n + recursiveSum(n - 1) #Recursive Function call

# Take input
num = int(input("Enter a number: "))

result = recursiveSum(num)
print(f"Sum of first {num} numbers is: {result}")
  