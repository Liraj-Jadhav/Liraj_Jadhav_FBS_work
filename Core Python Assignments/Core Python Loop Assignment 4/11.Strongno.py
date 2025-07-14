# 11. WAP to check if given number Strong Number.

# take input from user
num = int(input("Enter a number: "))
temp = num  # copy of the no.
facts_sum = 0

# Calculate sum of factorials of digits
while (temp > 0):

    d = temp % 10
    temp //= 10
    
    # Calculate factorial 
    fact = 1
    for i in range(1, d + 1):
        fact = fact * i
    
    facts_sum = facts_sum + fact

# Check Strong Number
if (facts_sum == num) :
    print(num," is a Strong Number.")
else:
    print(num, " is not a Strong Number.")
