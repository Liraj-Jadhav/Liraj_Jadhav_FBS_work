
# 6. Write a program to print Fibonacci series using recursion.

# Function definition
def fibbo(a,b,nt):
    if(nt >0):
        c=a+b
        print(c)

        fibbo(b,c,nt-1) # recursive function call


# take value of number of terms from user
nt= int(input("Enter number of terms Nt:"))
#function calling
fibbo(-1,1,nt)

