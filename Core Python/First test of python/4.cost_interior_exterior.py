"""
4. Calculate the cost of painting the following building’s walls
(both interior and exterior). You need to accept area and cost
of both interior and exterior wall.

"""

# take the inputs from the user
interior_area = float(input("Enter the total area of interior walls : "))
interior_cost = float(input("Enter the cost per square meter for painting interior walls: "))

exterior_area = float(input("Enter the total area of exterior walls : "))
exterior_cost = float(input("Enter the cost per square meter for painting exterior walls: "))

# Calculate cost of painting
total_interior_cost = interior_area * interior_cost
total_exterior_cost = exterior_area * exterior_cost

# Calculate total cost
total_cost = total_interior_cost + total_exterior_cost

# Show the result
print("Total cost For  painting the building is: Rs.",total_cost,"/sq.mtr")
