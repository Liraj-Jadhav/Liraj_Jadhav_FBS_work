# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# Take input celcius from user
celsius = float(input("Enter temperature in Celsius: "))

# formula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# Print the result
print("Temperature in Fahrenheit is:", fahrenheit)