"""
 11. Write a program to accept an integer amount from user and tell minimum
     number of notes needed for representing that amount.

"""
amount =int(input("Enter the Amount = "))  #5880

temp=amount

n500=amount//500    #11
amount=amount%500   #380

n200=amount//200    #1
amount=amount%200   #180

n100=amount//100    #1
amount=amount%100   #80

n50=amount//50      #1
amount=amount%50    #30

n20=amount//20      #1
amount=amount%20    #10

n10=amount//10      #1

print("Notes of Rs.500, Rs.200, Rs100, Rs.50, Rs.20, Rs.10 for given amount of Rs.",temp," are as follow : ")

print("No. of Notes of Rs.500 for given amount of Rs.",temp,"=",n500)
print("No. of Notes of Rs.200 for given amount of Rs.",temp,"=",n200)
print("No. of Notes of Rs.100 for given amount of Rs.",temp,"=",n100)
print("No. of Notes of Rs.50 for given amount of Rs.",temp,"=",n50)
print("No. of Notes of Rs.20 for given amount of Rs.",temp,"=",n20)
print("No. of Notes of Rs.10 for given amount of Rs.",temp,"=",n10)



