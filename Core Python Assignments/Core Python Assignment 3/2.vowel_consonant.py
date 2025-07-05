
# 2. Write a program to input any alphabet and check whether it is vowel or consonant.


alpha = input("Enter a Character : ")

#if (alpha =='a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u'):

if(alpha in 'aeiouAEIOU'):
    print(alpha," is the vowel.")

else:
    print(alpha," is the consonant.")
