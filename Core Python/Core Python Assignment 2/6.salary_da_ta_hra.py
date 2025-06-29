"""
6. Write a Program to calculate total salary of employee based on basic, da=10% of basic,
ta=12% of basic, hra=15% of basic.

"""

# Take input basic salary
basic = float(input("Enter basic salary: "))

# Calculate DA, TA, and HRA
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

# Calculate total salary
total_salary = basic + da + ta + hra

# Display the result
print("Total Salary is:", total_salary)



