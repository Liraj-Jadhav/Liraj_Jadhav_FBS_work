
# 5. Write a Program to calculate the selling price of a book base on cost price and discount

# here we take input of  Cost price and discount
cost_price = float(input("Enter the cost price of the book: "))
discount = float(input("Enter the discount percentage: "))

# we Calculate discount amount
discount_price = (cost_price * discount) / 100

# we Calculate selling price
selling_price = cost_price - discount_price

# Result the selling price
print("Selling Price of the book is:", selling_price)
