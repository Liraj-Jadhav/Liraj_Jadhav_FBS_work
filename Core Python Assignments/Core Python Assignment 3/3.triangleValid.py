#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

An1 = int(input("Enter Angle1 = "))
An2 = int(input("Enter Angle2 = "))
An3 = int(input("Enter Angle1 = "))

if (An1+An2+An3 == 180) :

    print("Sum of all three Angles- Angle1:",An1,"Angle2:",An2,"& Angle3:",An3,"= 180 Degree, So Its is Valid Triangle")

else:

    print("Sum of all three Angles- Angle1:",An1,"Angle2:",An2,"& Angle3:",An3,"!= 180 Degree, So It is not a Triangle")
