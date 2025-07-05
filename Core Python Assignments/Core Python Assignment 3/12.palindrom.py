# 12. Write a program to check if given 3 digit number is a palindrome or not.


num = int(input("Enter the number : "))  #121

temp=num

a=num%10    
num=num//10  
b=num%10   
reverse=(a*10)+b   
c=num//10
reverse=(reverse*10)+c

if(temp== reverse):

    print("Reverse of three digit no.",temp,"=",reverse," are same no so it is palindhrom no")

else:
    print("it is not palindhrome")



    