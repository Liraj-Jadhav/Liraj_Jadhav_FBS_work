"""
      Function Type-4 - 
Function With Parameter, With Return Value Type

10. Write a program to check if entered year is a leap year or not.

"""
def isLeapYear(year):
    # A year is a leap year if it is divisible by 4
    # but not by 100 unless it is also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Main program
year = int(input("Enter a year: "))


if isLeapYear(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")