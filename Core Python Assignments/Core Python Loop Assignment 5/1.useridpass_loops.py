"""
# 1. Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate.

"""

# Good credentials
right_user_id = "Liraj"
right_password = "8459"

# Maximum number of trying
max_trys = 3

trys = 1

while (trys <= max_trys):
    print("This is your try number:", trys) 

    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if (user_id == right_user_id and password == right_password):
        print("Login Successfully")
        break
    else:
        print("Incorrect User ID or Password. Please try again.")
    
    trys += 1

# terminated message
if (trys > max_trys):
    print("Maximum attempts reached. Program terminated.")
