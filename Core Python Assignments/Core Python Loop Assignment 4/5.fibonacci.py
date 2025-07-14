# 5.WAP to print Fibonacci series upto n.

n = int(input("Enter the Number : "))

a=1
b=0

print("Fibonacci series upto",n,"is : ")
for x in range( 1, n+1):
    c= a+b
    print(c)
    a=b
    b=c


     

