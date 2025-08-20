"""
         Function Type-4 - 
Function With Parameter, With Return Value Type

1. Write a program to calculate area of Rectangle

"""
# Function with parameters and return type
def areaOfRectangle(length, width):
    area = length * width
    return area

# Take input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and store the result
area = areaOfRectangle(length, width)

# Display the result
print(f"Area of rectangle with length {length} and width {width} is {area}")
