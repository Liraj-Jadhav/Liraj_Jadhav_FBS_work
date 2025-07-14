
# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

# Accepting input from the user
n = int(input("Enter the number : "))

print("The numbers or integers upto Given number",n,"that aren't divisible by 2 & 3 are : ")

for i in range(1, n + 1):
    if (i % 2 != 0 and i % 3 != 0):
    
        print(i)

