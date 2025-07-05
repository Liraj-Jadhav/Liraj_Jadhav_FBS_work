# 1. Write a program to check if the given number is positive or negative.

# Step 1: Take input from the user
number = float(input("Enter a number: "))

# Step 2: Use if-else to check sign
if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is neutral and So it is Zero.")