# List Exercise 1
ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
# Organizing the list
ages.sort()
print(max(ages))
# Removing the duplicates
print(list(dict.fromkeys(ages)))

