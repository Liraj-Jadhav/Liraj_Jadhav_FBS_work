
"""
# 6.e -
         * 
       * * * 
     * * * * * 
   * * * * * * * 
 * * * * * * * * * 

"""
# My method=

for i in range(1,6):   
    for j in range(1,7-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")

    for j in range(1, i):
        print("*",end=" ")
    print()
    
"""

for i in range(1, 6):                     # Rows 1 to 5
    for j in range(1, 6 - i):             # Print spaces
        print(" ", end=" ")

    for j in range(1, 2 * i):             # Print stars
        print("*", end=" ")
    
    print()

"""