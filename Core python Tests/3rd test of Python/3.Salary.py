#3. Salary program with da , ta , hra

n = int(input("Enter number of employees: "))
grand_total = 0

for i in range(1, n + 1):
    basic = float(input(f"Enter basic salary for employee {i}: "))

    # basic salary with da , ta, hra  
    if basic < 20000:
        da = 0.10 * basic   # 10%
        ta = 0.12 * basic   # 12%
        hra = 0.15 * basic  # 15%
    else:
        da = 0.15 * basic   # 15%
        ta = 0.18 * basic   # 18%
        hra = 0.20 * basic  # 20%

    total = basic + da + ta + hra
    print(f"Employee {i} total salary = {total}")

    grand_total += total

print(f"\nGrand total for all employees = {grand_total}")
