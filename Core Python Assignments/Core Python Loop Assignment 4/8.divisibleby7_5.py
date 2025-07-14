# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start = int(input("Enter start: "))
end = int(input("Enter End: "))

print("Numbers divisible by 7 and multiple of 5 from given range",start,"to",end," are:")

for num in range(start, end + 1):
    if (num % 7 == 0 and num % 5 == 0) :
        print(num)