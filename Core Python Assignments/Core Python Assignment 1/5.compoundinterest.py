# 5. Write a program to enter P, T, R and calculate Compound Interest.

p = float(input("Enter Principal amount P = "))
t = float(input("Enter Time in years T = "))
r = float(input("Enter Rate of Interest R = "))
amount = p * (1 + r / 100) ** t
compound_interest = amount - p

print("Compound Interest = ",compound_interest)