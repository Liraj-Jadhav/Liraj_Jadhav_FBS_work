
"""
8.b. write a Program to solve the following series 
b. N + N^2 + N^3 + ... + N^N

"""

n = int(input("Enter the value of N: "))

sum=0

for i in range (1,n+1):

    ans=n**i
    sum += ans

print("Sum of the series N + N^2 + ... + N^N is: ", sum)