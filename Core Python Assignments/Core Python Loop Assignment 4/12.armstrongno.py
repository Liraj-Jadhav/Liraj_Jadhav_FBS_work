# 12. WAP to print Armstrong number within a given range

start = int(input("start: "))
end = int(input("end: "))

print("Armstrong numbers within the given range",start,"to",end,"are: ")

for a in range(start, end + 1):
    temp = a
    num_of_digits = 0

    # Counting the digits
    while (temp > 0) :
        num_of_digits += 1
        temp //= 10

    temp = a # Reset temp = original number
    add_powers = 0  #addition of powers

    # Calculate sum of digits raised to power num_of_digits
    while (temp > 0) :
        digit = temp % 10

        #add_powers = add_powers + digit ** num_of_digits 
        add_powers += digit ** num_of_digits
       
        temp = temp // 10   # temp //= 10

    if (a == add_powers) :
        print(a)
