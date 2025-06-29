# 10. Write a program to calculate area of an equilateral triangle.

# take side length from user
side = float(input("Enter the length of the side of an equilateral triangle = "))

# calculate area
area = (3 ** 0.5 / 4) * (side * side)

#  result
print("Area of an equilateral triangle is:", area)