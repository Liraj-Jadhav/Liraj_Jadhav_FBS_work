
# 7. Write a program to find sum of digits using recursion.

def sumOfDigit(num):
    if(num==0):
        return 0
    else:
        a=num%10
        return a+sumOfDigit(num//10) # recursive function call

num=int(input("enter Number of terms: "))
print(sumOfDigit(num))