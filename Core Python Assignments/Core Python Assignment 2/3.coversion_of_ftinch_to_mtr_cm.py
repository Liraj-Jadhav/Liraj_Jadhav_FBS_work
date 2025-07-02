# 3. Write a program to convert distance given in feet and inches into meter and centimeter

# Take input 
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter inches: "))

# Convert the total distance to inches
total_inches = (feet * 12) + inches

# Convert inches to centimeters 
centimeters = total_inches * 2.54 #(1 inch = 2.54 cm)

# Convert centimeters to meters and centimeters
meters = int(centimeters // 100)
cm = centimeters % 100

# Print the output
print("Distance is:", meters, "meters and", cm, "centimeters")
