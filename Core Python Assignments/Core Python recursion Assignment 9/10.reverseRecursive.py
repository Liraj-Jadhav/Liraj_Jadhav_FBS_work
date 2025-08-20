
# 10. Write a program to reverse a number using recursion.


# Function definition
def reverseNumber(num, rev):
    if num != 0:
        a = num%10
        rev = rev * 10 +a
        return reverseNumber(num//10,rev) # Recursive function Call
    else:
        return rev


# Taking input from user
num = int(input("Enter a number: "))

# Calling the recursive function
ans = reverseNumber(num,0)

print("Reversed number:", ans)