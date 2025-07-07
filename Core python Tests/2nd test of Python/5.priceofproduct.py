# 5. Price of the 5 product

p1 = float(input("price of product 1: "))
p2 = float(input("price of product 2: "))
p3 = float(input("price of product 3: "))
p4 = float(input("price of product 4: "))
p5 = float(input("price of product 5: "))

# with no gst
total_price = p1 + p2 + p3 + p4 + p5

# gst
gst = (18 / 100) * total_price

# amount with 18 % gst
final_bill = total_price + gst

# result final bill
print("Total bill amount after adding 18% GST is: Rs.", final_bill)
