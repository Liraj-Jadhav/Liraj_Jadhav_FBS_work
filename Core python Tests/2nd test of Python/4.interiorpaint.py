# interior painting of 4 equal size walls

# Accept l and b
l = float(input("Enter the length of the wall: "))
b = float(input("Enter the breadth of the wall: "))

# take cost per square unit 
cost = float(input("The cost of painting per square unit: "))

# Calculate area of one wall
wall_area = l * b

# full area of 4 walls
totalarea = 4 * wall_area

# total cost
totalcost = totalarea * cost

# Result  = the total cost
print("Total cost of painting the interior of the building is Rs.:", totalcost)
