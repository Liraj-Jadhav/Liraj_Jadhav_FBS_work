"""
# 6. Write a Program to input two angles from user and find third angle of the
triangle.

"""
angle1 = float(input("Enter the  angle1 of the triangle: "))
angle2 = float(input("Enter the  angle2 of the triangle: "))

angle3 = 180 - (angle1 + angle2)

print("The angle3 of the triangle is:", angle3)