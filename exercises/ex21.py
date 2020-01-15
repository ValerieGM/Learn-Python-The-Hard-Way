def add(a, b):
    print(f"{a} + {b}")
    return a + b

def subtract(a, b):
    print(f"{a} - {b}")
    return (a - b)

def multiply(a, b):
    print(f"{a} * {b}")
    return a * b

def divide(a, b):
    print(f"{a} / {b}")
    return a / b

print("Mathemathical Functions::")

age = add(10, 9)
height = subtract(90, 10)
weight = multiply(50, 2)
iq = divide(120, 2)

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

calc = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print('Complex calculation:: ', calc)
