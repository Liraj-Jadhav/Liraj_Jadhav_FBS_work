"""
# 2. Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.

"""
no_stds = int(input("Enter number of students: "))

ttl_perct = 0  # store total overall percentages

for student in range(1, no_stds + 1):
    print("Enter marks for 5 subjects of Student", student)
    total_marks = 0

    for sub in range(1, 6):
        print("Enter marks for Subject", sub)
        marks = float(input())  
        total_marks += marks

    percentage = (total_marks / 500) * 100
    print("Percentage of Student", student, "is", percentage, "%")

    ttl_perct += percentage 

avg_perct = ttl_perct/ no_stds
print("Average Percentage of all students is", avg_perct, "%")