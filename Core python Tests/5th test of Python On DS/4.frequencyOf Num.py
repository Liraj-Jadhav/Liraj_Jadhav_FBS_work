# 4. Frequency of the numbers in given list

# Given list
numbers = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

# Empty dictionary to store frequency
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1   # already present
    else:
        freq[num] = 1    # first time getting number

print("Frequency dictionary:", freq)
