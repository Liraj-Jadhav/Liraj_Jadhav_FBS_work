"""
# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene
triangle.

"""
s1 = int(input("Enter side1 = "))
s2 = int(input("Enter side2 = "))
s3 = int(input("Enter side3 = "))

if(s1 == s2 ==s3):
    print("It is the equilateral triangle.")

elif(s1==s2 or s2==s3 or s1==s3):
    print("It is isosceles  triangle.")

else:
    print("it is scelen triangle.")


