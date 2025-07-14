# 9. WAP to print all numbers in a range divisible by a given number.

start = int(input("start: "))
end = int(input("end : "))
divisor = int(input("divisor: "))

print("All the number in the given range",start,"to",end," divisible by given number",divisor,"are :")

for num in range(start, end + 1):
    if num % divisor == 0:
        print(num)