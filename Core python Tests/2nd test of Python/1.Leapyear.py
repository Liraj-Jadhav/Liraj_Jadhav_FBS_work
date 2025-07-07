# 1. Leap year program 

#  Take input year
year = int(input("Enter the year: "))

# check conditions
if (year % 4 == 0 and year % 100 != 0 and year % 400 != 0):
   
   print (year," is the Leap Year")

else:
   
   print(year,"is not a Leap Year")