"""
11. Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.

"""
a1 = int(input("Age1 = "))
a2 = int(input("Age2 = "))
a3 = int(input("Age3 = "))
a4 = int(input("Age4 = "))
a5 = int(input("Age5 = "))

#100
ticket_amt = int(input("Enter the ticket amount : "))

final_amt = 0

# Age1
if(a1<12):
    final_amt += ticket_amt - (ticket_amt * 0.3)

elif(a1>59):
    final_amt += ticket_amt - (ticket_amt *  0.5)

else:
    final_amt += ticket_amt
# Age2
if(a2<12):
    final_amt += ticket_amt - (ticket_amt * 0.3)

elif(a2>59):
    final_amt += ticket_amt - (ticket_amt * 0.5)

else:
    final_amt += ticket_amt

# Age3
if(a3<12):
    final_amt += ticket_amt - (ticket_amt * 0.3)

elif(a3>59):
    final_amt += ticket_amt - (ticket_amt * 0.5)

else:
    final_amt += ticket_amt

# Age4
if(a4<12):
    final_amt += ticket_amt - (ticket_amt * 0.3)

elif(a4>59):
    final_amt += ticket_amt - (ticket_amt * 0.5)

else:
    final_amt += ticket_amt

# Age5
if(a5<12):
    final_amt += ticket_amt - (ticket_amt * 0.3)

elif(a5>59):
    final_amt += ticket_amt - (ticket_amt * 0.5)

else:
    final_amt += ticket_amt

# Result = total Amount of the ticket
print("Total amount of the ticket for all 5 different  ages people is Rs",final_amt)

