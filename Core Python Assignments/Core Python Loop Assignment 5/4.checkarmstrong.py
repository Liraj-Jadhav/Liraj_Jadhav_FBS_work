"""
4. Write a program to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)

"""
# take a number from user
num = int(input("Enter a number: "))

temp = num # copy num in temp variable

# to get the no. of digits
n = 0
while temp > 0:
    temp = temp // 10
    n += 1   # n = n+1

# again store original no. store in the temp
temp = num
sum = 0

# Calculate the sum of digits raised to the power n
while temp > 0:
    digit = temp % 10
    sum += digit ** n # sum = sum + digit**n
    temp = temp // 10

# verifying  sum is equal to the original number or not ?
if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
