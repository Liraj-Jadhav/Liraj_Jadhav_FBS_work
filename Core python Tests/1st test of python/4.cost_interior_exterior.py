"""
4. Calculate the cost of painting the following building’s walls
(both interior and exterior). You need to accept area and cost
of both interior and exterior wall.

"""

#take the inputs
side = int(input("Enter the no. of Rooms = "))
cost_inte = int(input("Enter the cost of internal painting : "))
cost_exte = int(input("Enter the cost of External painting : "))

totalarea = 4 * side * side

totalcost = totalarea * cost_inte+ totalarea * cost_exte

print("Total cost of painting 2 rooms  Rs.",2*totalcost,"/Sq.mtr" )