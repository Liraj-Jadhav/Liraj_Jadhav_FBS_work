#Sum of the series

n = int(input("Enter n: "))   
fact = 1                     
total = 0               

for i in range(1, n + 1):
    fact *= i             
    total += i / fact        

print(f"Sum of series = {total}")
