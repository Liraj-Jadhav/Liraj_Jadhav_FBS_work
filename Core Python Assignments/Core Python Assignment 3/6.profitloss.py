# Write a  Program to calculate Profit or Loss

# take input from user
cp = float(input("Enter the Cost Price (CP): "))
sp = float(input("Enter the Selling Price (SP): "))


# Calculate profit or loss
if sp > cp:
    profit = sp - cp
    print("the Profit = Rs.", profit)

elif sp < cp:
    loss = cp - sp
    print("the Loss = Rs.", loss)
else:
    print("The Cost Price and Selling Price are Equal, So there No Loss or Profit.")