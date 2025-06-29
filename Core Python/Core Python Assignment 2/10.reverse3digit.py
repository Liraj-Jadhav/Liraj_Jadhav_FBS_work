# 10. Write a program to reverse three-digit number.

num = int(input("Enter the number : "))  #128
temp=num
a=num%10    #8
num=num//10  #12
b=num%10    #2
reverse=(a*10)+b   #82
c=num//10
reverse=(reverse*10)+c


print("Reverse of three digit no.",temp,"=",reverse)


"""
num = int(input("Enter the number : "))  #128

a=num%10    #8
b=num//10  #12
c=b%10    #2
d=b//10   #1

reverse=(a*100)+(c*10)+d

print("Reverse of three digit no.",num,"=",reverse)

"""