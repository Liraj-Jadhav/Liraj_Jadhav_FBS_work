# Denomination of the notes

# Denominations
D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))  #Amount = 8385

if amount < 0:
    print("Amount cannot be negative.")

else:
    counts = []
    balance_amt = amount # here i take temparory variable balance_amt
    for d in D:
        if balance_amt == 0:
            break
        cnt = balance_amt // d
        
        if cnt:
            counts.append((d,cnt))
            balance_amt -= cnt * d

    # Output
    total_notes = 0
    for pair in counts:
        total_notes += pair[1]   # add the count part
    print(f"Minimum notes for ₹{amount}: {total_notes}")

    for pair in counts:
        print(f"₹{pair[0]}: {pair[1]}")