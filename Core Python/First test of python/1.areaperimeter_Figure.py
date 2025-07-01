# Area and Perimter of The give Figure
l= float(input("Enter the length of rectangle: "))
b= float(input("Enter the breadth of rectangle: "))
r = float(input("Enter the radius of half circle: "))

# Calculate area and perimeter of rectangle
rect_area = l * b
rect_perimeter = 2 * (l + b)

#  Calculate area and perimeter of halfcircle
pi = 3.1416
halfcircle_area =( pi * r* r)/2
halfcircle_perimeter = (2 * pi * r)/2

#Calculate the area  and perimeter of the figure

totalarea_figure= rect_area + halfcircle_area

totalperimeter_figure= rect_perimeter + halfcircle_perimeter

print("total area of the figure = ", totalarea_figure)
print("totalperimeter of the figure = ", totalperimeter_figure)
