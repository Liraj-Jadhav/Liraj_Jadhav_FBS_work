# 8.e.Solve thefollowing series-   x - x2/3 + x3/5 - x4/7 + .... to n terms

x= int(input("enter x: "))
n = int(input("enter n: "))

sum=0

for i in range (1,n+1):

    term =(x**i)/(2*i)-1

    if(i%2 == 0):
        sum -= term
    else:
        sum += term

print("Sum of the series  x - x2/3 + x3/5 - x4/7 + .... to n terms : ",sum)
