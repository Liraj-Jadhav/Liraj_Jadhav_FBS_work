
# 4. Write a program to enter P, T, R and calculate simple Interest.

p = int(input("enter principle amount = "))
years = int(input("enter no. of years = "))
rate = float(input("enter rate of interest = "))

interest = (p* years * rate)/100

print ("Simple interest = ",interest)