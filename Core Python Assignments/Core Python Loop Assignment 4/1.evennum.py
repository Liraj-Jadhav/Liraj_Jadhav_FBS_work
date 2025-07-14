# for Loop

# 1. WAP to print all even numbers until n.

n = int(input("Enter Number n : "))

print ("Even number until",n,"are :")

for i in range(0, n + 1):
    if i % 2 == 0:
        print(i)