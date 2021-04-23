# List Exercise 2
ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
ages1 = [2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]

# Defining a function


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result


print(common_data(ages, ages1))
