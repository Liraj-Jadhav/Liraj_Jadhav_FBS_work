"""
6.a 

* * * * * 
*       * 
*       * 
*       * 
*       * 
* * * * * 

"""
for i in range(0, 6):       # 6 rows: 0 to 5
    for j in range(0, 5):   # 5 columns: 0 to 4
        if i == 0 or i == 5 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

