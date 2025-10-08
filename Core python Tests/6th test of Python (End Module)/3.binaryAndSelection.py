
# Function Definition -  Selection Sort -
def selectionSort(list1):
     for i in range (len(list1)):
          index= i
          min= list1[i]

          for j in range (i+1,len(list1)):
               
               if(min > list1[j]):

                    min = list1[j]
                    index = j
          
          list1[i],list1[index] = list1[index],list1[i]

     return list1


# Binary Searching
def binarySearch(sorted_list1,x):
    start = 0
    end =len(sorted_list1) - 1

    while (start <=end):

        mid =(start + end) // 2

        if(sorted_list1[mid] == x):
            return mid
        
        if(sorted_list1[mid] > x):  #left
            end = mid - 1

        else:
            start = mid + 1

    return -1



# Taking list1 from user
list1=[]

num =int(input("Enter the number of element"))

for i in range(num):
    element=int(input(f"enter the element {i+1} :"))
    list1.append(element)

print(f"Given List of the elements : {list1}")



# Function Calling
sorted_list1=selectionSort(list1)

print(f"Sorted_list1 = {sorted_list1}\n")




# binary Search

x= int(input("Enter the the number to be Found from our sorted_list1: ")) # Number to be found

#function calling for binary searching
result = binarySearch(sorted_list1,x) 

if(result == -1):

    print(f"{x} is Not present in the list {sorted_list1}")

else:
    print(f"{x} is  Present in the list {sorted_list1}")
 

 