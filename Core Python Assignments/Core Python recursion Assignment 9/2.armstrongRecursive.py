"""
# 2. Write a program to check if given number is Armstrong or not - (using recursive
     function.)

"""


def count(num): # function definition for counting digit

    if(num != 0):
        return 1+ count(num // 10) #Recursive function call for counting digit
    else:
        return 0

def armstrong(num,c): #Calculate armstrong sum
    if num == 0:
        return 0
    else:
        digit = num % 10
        return (digit ** c) + armstrong(num // 10, c)   # Recursive call
 
# take number from user
num= int(input("Enter the number = "))

c = count(num) # storing and function calling to count digit

ans = armstrong(num,c) #storing and function calling to calulate Armstrong sum

if(ans == num): # checking  condition for the armstrong number
    print(f"{num} is an Armstrong Number")

else:
    print(f"{num} is not an Armstrong number")