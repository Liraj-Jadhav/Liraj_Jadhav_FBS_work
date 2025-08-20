def power(m, n):
    # Base case
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)

# Take input
m = int(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))

result = power(m, n)
print(f"{m}^{n} = {result}")
