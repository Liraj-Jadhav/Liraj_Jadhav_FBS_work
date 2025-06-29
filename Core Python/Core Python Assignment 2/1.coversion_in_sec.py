# 1. Write a program to Covert the time entered in hrs, minutes and seconds into seconds

# Take input 
hours = int(input("Enter hrs: "))
minutes = int(input("Enter mins: "))
seconds = int(input("Enter secs: "))

# Convert hrs,mins and secs into seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# Print the result
print("Total time in seconds is:", total_seconds)
