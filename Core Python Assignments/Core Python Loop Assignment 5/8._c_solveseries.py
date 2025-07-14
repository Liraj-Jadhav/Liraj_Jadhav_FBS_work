# 8.c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

# take the input number of terms from user
n = int(input("Enter the number of terms: "))

term = 1   
sum = 0

print("Geometric series terms are:")

for i in range(n):
    print(term, end=" ")
    sum += term
    term *= 2   # Multiply by common ratio (2)

print("\nSum of geometric series is:", sum)