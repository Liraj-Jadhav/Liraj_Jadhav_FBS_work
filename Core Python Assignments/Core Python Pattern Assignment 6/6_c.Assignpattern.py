"""
6.c Pascal triangle pattern of numbers

      1   
    1   1   
  1   2   1   
1   3   3   1 

"""


x = 4  # Number of rows

for i in range(0, x):

    for j in range(0, x - i - 1):
        print("  ", end="")

    
    num = 1
    for j in range(0, i + 1):
        print(num, end="   ")#num printing
        num = num * (i - j) // (j + 1)
    
    print()
