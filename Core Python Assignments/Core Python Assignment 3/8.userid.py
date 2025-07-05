"""
8. Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)

"""
import random

userid = input("User Id : ")
password = input("Password :")

if(userid == "Liraj17" and password == "845950"):

    captcha = random.randint(1000,9999)
    print("Capcha: ",captcha)
    user_captcha = int(input("Enter Captcha : "))
    
    #compare input and captcha
    #if Correct, Successful Login
   
    #if not, its wrong captcha
    #If Credential are wrong , unsuccessful Login
        
    if (captcha == user_captcha):

        print("Captcha is correct, So It is Successful Login")

    else:

        print("captcha is not correct")
else:
    print("Credential are wrong , So It is Unsuccessful login")

    