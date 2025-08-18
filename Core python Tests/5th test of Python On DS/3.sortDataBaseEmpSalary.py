Data = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Tannu", 14000],
    [320, "Suresh", 35000]
]

# define a function that returns salary from each employee
def get_salary(emp):
    return emp[2]

# sort using the function
sorted_data = sorted(Data, key=get_salary)

print("Employees sorted list base on Employees's salary:")
for emp in sorted_data:
    print(emp)
