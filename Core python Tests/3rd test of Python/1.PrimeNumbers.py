#first N prime numbers
#input
start = int(input("Enter lower start: "))
end   = int(input("Enter end: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num < 2:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else: 
        print(num)
