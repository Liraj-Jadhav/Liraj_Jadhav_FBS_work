# 8.d. write a program to solve the following series -d>  S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

# Take value of a from user
a = int(input("Enter the value of a: "))

sum = 0

# Loop from 1 to 10 
for i in range(1, 11):
    term = (a ** i) / i
    sum += term

print("Sum of the series a + a2 / 2 + a3 / 3 + ...... + a10 / 10 is:", sum)
