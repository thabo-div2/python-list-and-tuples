x = tuple(input("Enter your numbers here: "))

print(str(max(x)))
print(str(min(x)))
a = sum(str(x))
print(a)

if type(x) == tuple:
    x = list(x)
    x.append(input("Add more numbers: "))
    print(str(tuple(x)))



