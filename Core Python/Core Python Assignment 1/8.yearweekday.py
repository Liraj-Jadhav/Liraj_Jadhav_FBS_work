# 8.First program to convert total days into years, weeks, and days

total_days = int(input("Enter no. of days: "))

#  Calculations of year, week and days
years = total_days // 365
lefts = total_days % 365
weeks = lefts // 7
days = lefts % 7

# print Output statement
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)
