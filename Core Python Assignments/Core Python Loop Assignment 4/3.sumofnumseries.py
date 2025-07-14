
# 3. WAP to print sum of series upto n.

# input n
n = int(input("Enter the number (n): "))

series_sum = 0

# find the sum of series upto the number
for i in range(1, n + 1):

    series_sum += i  

print("The sum of series until", n, "is:", series_sum) 