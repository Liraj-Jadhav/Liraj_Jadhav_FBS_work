# Program to find union of two lists without using set

# Take input from user
list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))
print(list1)
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))
print(list2)

union_list = list1[:]   # copy all elements of list1

for item in list2:
    if item not in union_list:   # add only if not already present
        union_list.append(item)

print("Union of the two lists:", union_list)
