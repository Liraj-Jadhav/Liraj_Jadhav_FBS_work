"""
# Write a program to check if person is eligible to marry or not (male age >=21 and
female age>=18)

"""

boy_age =int(input("enter the age of boy :"))
girl_age =int(input("enter the age of girl :"))

#check Boy eligibility to get Marry
if(boy_age >= 21):
    print("Boy age is ",boy_age,"years old Which is above 21, So the boy is eligible for marry")
else :
    print ("Boy age is ",boy_age,"years old Which is below 21, So the boy is not eligible for marry")
    

#check girl eligibility to get marry

if(girl_age >= 18):
    print("Girl age is ",girl_age,"years old Which is above 18, So the Girl is eligible for marry")
else :
    print("Girl age is ",girl_age,"years old Which is below 18, So the Girl is not eligible for marry")
    
