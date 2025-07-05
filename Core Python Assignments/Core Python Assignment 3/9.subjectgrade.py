#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

mark1 = float(input("Enter marks of Subject 1 : "))
mark2 = float(input("Enter marks of Subject 2 : "))
mark3 = float(input("Enter marks of Subject 3 : "))
mark4= float(input("Enter marks of Subject 4: "))
mark5 = float(input("Enter marks of Subject 5: "))

# Condition for Class And Grade
# Subject 1
if (mark1 >= 80 and mark1 <=100):
    print("Marks of Subject 1 is ",mark1, "% So the Resul = Distinction Class and Grade = A")
elif( mark1 >= 70 and mark1  < 80):
    print("Marks of Subject 1 is ",mark1,"% So the Result= First Class and Grade = B")
elif (mark1 >= 60 and mark1  < 70):
    print("Marks of Subject 1 is ",mark1,"% So the Result = Higer  Second Class and Grade = C")
elif (mark1 >= 50 and mark1 < 60):
    print("Mark of Subject 1 is  ",mark1,"% So the Result = Second Class and Grade = D")
elif (mark1>= 40 and mark1 < 50):
    print("Marks of Subject 1 is ",mark1,"% So the Result = Third Class and Grade = E") 
else:
    print("Marks of Subject 1 is ",mark1,"% So the Result = Fail Class and Grade = F") 

# Sunject 2
if (mark2 >= 80 and mark2 <=100):
    print("Marks of Subject 2 is ",mark2, "% So the Resul = Distinction Class and Grade = A")
elif( mark2 >= 70 and mark2  < 80):
    print("Marks of Subject 2 is ",mark2,"% So the Result= First Class and Grade = B")
elif (mark2 >= 60 and mark2  < 70):
    print("Marks of Subject 2 is ",mark2,"% So the Result = Higer  Second Class and Grade = C")
elif (mark2 >= 50 and mark2 < 60):
    print("Mark of Subject 2 is  ",mark2,"% So the Result = Second Class and Grade = D")
elif (mark2>= 40 and mark2 < 50):
    print("Marks of Subject 2 is ",mark2,"% So the Result = Third Class and Grade = E") 
else:
    print("Marks of Subject 2 is ",mark2,"% So the Result = Fail Class and Grade = F")  

# Subject 3

if (mark3 >= 80 and mark3 <=100):
    print("Marks of Subject 3  is ",mark3, "% So the Resul = Distinction Class and Grade = A")
elif( mark3 >= 70 and mark3  < 80):
    print("Marks of Subject 3 is ",mark3,"% So the Result= First Class and Grade = B")
elif (mark3 >= 60 and mark3  < 70):
    print("Marks of Subject 3 is ",mark3,"% So the Result = Higer  Second Class and Grade = C")
elif (mark3 >= 50 and mark3 < 60):
    print("Mark of Subject 3 is  ",mark3,"% So the Result = Second Class and Grade = D")
elif (mark3>= 40 and mark3 < 50):
    print("Marks of Subject 3 is ",mark3,"% So the Result = Third Class and Grade = E") 
else:
    print("Marks of Subject 3 is ",mark3,"% So the Result = Fail Class and Grade = F")  

# Subject 4

if (mark4 >= 80 and mark4 <=100):
    print("Marks of Subject 4 is ",mark4, "% So the Resul = Distinction Class and Grade = A")
elif( mark4 >= 70 and mark4  < 80):
    print("Marks of Subject 4 is ",mark4,"% So the Result= First Class and Grade = B")
elif (mark4 >= 60 and mark4  < 70):
    print("Marks of Subject 4 is ",mark4,"% So the Result = Higer  Second Class and Grade = C")
elif (mark4 >= 50 and mark4 < 60):
    print("Mark of Subject 4 is  ",mark4,"% So the Result = Second Class and Grade = D")
elif (mark4>= 40 and mark4 < 50) :
    print("Marks of Subject 4 is ",mark4,"% So the Result = Third Class and Grade = E") 
else:
    print("Marks of Subject 4 is ",mark4,"% So the Result = Fail Class and Grade = F")  

# Subject 5

if (mark5 >= 80 and mark5 <=100):
    print("Marks of Subject 5 is ",mark5, "% So the Resul = Distinction Class and Grade = A")
elif( mark5 >= 70 and mark5  < 80):
    print("Marks of Subject 5 is ",mark5,"% So the Result= First Class and Grade = B")
elif (mark5 >= 60 and mark5  < 70):
    print("Marks of Subject 5 is ",mark5,"% So the Result = Higer  Second Class and Grade = C")
elif (mark5 >= 50 and mark5 < 60):
    print("Mark of Subject 5 is  ",mark5,"% So the Result = Second Class and Grade = D")
elif (mark5 >= 40 and mark5 < 50) :
    print("Marks of Subject 5 is ",mark5,"% So the Result = Third Class and Grade = E") 
else:
    print("Marks of Subject 5 is ",mark5," which is below 40 So the Result = Fail Class and Grade = F")  