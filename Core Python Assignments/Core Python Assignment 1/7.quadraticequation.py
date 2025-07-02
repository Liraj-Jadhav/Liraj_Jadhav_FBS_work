# 7. Program to Find the Roots of a Quadratic Equation

a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))

ans = (b*b) - (4*a*c)
ans = ans ** 0.5

root1 = (-b + ans)/ (2 * a)
root2 = (-b - ans)/ (2 * a)

print("Root1= ",root1)
print("Root2= ",root2)