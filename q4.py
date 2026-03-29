#queastion 4

a, b, c = map(int, input("Enter three numbers: ").split())

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print(largest, "is the largest number")