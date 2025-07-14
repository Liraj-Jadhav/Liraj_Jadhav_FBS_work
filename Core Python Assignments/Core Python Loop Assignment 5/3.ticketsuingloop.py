"""
# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.

"""
# take input number of passengers and per ticket cost
num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))

total_amount = 0

for i in range(1, num_passengers + 1): #use for loop for every passenger

    print("Enter age of passenger", i)
    age = int(input("age:"))

    if age < 12:
        discount = 0.30  # 30% discount
    elif age > 59:
        discount = 0.50  # 50% discount
    else:
        discount = 0.0   # No discount

  # passenger_cost = ticket_cost - (ticket_cost * discount)
    passenger_cost = ticket_cost * (1 - discount)  
    total_amount += passenger_cost

# Display total amount
print("Total ticket amount for all passengers:", total_amount)

