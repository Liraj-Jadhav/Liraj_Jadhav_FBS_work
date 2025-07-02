"""
# 1. Write a program to calculate the percentage of student based on marks of any 5
subjects.

"""

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

max_marks = 500


percentage = (total_marks / max_marks) * 100

print("percentage of student = ", percentage)

