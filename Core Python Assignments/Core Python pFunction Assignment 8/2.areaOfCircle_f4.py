"""
         Function Type-4 - 
Function With Parameter, With Return Value Type

2. Write a program to calculate area of circle

"""
# Function with parameter and return type
def areaOfCircle(r):
    area = 3.14 * r * r
    return area

# Take input from user
r = float(input("Enter radius of circle r = "))

# Call the function and store the result
area = areaOfCircle(r)

# Print the result
print(f"Area of Circle of radius {r} is {area}")