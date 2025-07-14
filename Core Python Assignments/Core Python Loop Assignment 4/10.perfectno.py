# 10. WAP to check if given number is Perfect Number.

num = int(input("Enter a number: "))
divisors_add = 0  #divisors addition

for i in range(1, num):
    if num % i == 0:
        divisors_add += i

if (divisors_add == num) : # condition for perfect number
    print(num, "is a Perfect Number.")
else:
    print(num, "is not a Perfect Number.")