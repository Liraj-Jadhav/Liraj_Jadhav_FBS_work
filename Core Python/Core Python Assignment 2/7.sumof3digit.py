# 7. Write a program to Find the sum of 3 digit number

#type 1-

num= int(input( "Enter the number : ")) # 427

a = num%10
b=num//10
c=b%10
d=b//10

sum_of_digit=a+c+d

print("sum of three digit number",num,"=",sum_of_digit)


"""
#type-2=

num= int(input( "Enter the number : ")) # 327

a = num%10
num=num//10
b=num%10
c=num//10

sum=a+b+c

print("sum of three digit number",num,"=",sum)

"""
