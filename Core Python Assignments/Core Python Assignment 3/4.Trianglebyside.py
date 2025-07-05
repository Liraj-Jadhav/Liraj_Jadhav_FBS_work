"""
#4. Write a program to input all sides of a triangle and check whether triangle is valid or
not.

"""
#  Take input of three sides  of the triangle from user
s1 = float(input("Enter side1: "))
s2 = float(input("Enter side2: "))
s3 = float(input("Enter side3: "))

# Check triangle valid or not
if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print("The triangle is valid.")
else:
    print("The triangle is Not valid.")
