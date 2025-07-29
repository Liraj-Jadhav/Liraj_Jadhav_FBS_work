"""
6.g - 
        A 
      A B C 
    A B C D E 
  A B C D E F G 
A B C D E F G H I 

"""


for i in range(1, 6):                     # Rows from 1 to 5
    for j in range(1, 6 - i):             # Spaces for centering
        print(" ", end=" ")

    a = 65                      # ASCII value of 'A'
    for j in range(1, 2 * i):            # Characters in row
        print(chr(a), end=" ")
        a += 1

    print()
