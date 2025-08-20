
"""
      Function Type-4 - 
Function With Parameter, With Return Value Type

6. Write a program to find print the following Fibonacci series using
functions:
1 1 2 3 5 8 n terms

"""
# Function with parameter and return value
def fibonacciSeries(n):
    a = 1
    b = 0
    print("Fibonacci series up to", n, "terms is:")
    for x in range(1, n+1):
        c = a + b
        print(c)
        a = b
        b = c
    
    return 0 

# Main code
n = int(input("Enter the Number: "))

# Call the function
result = fibonacciSeries(n)
