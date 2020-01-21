v = 0
numbers = []

while v < 6:
    print(f"At the top v is {v}")
    numbers.append(v)

    v += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom v is {v}")

print("The numbers: ")

for num in numbers:
    print (num)
