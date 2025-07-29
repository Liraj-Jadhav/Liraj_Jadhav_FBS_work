
"""
# 7.e = 

        1   
      1   2   
    1       3
  1           4
1   2   3   4   5

"""

n = 5  # number of rows

for i in range(1, n + 1):
    # Print leading spaces
    print("  " * (n - i), end="")

    for j in range(1, i + 1):
        # First row, last row: print all numbers
        # Other rows: print only first and last number in the row
        if j == 1 or j == i or i == n:
            print(j, end="   ")
        else:
            print("    ", end="")  # Print space in place of missing number

    print()  # Move to next line
