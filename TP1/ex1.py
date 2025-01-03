a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

addition = a + b
subtraction = a - b
multiplication = a * b

if b != 0:
    division = a / b
    floor_division = a // b
    modulus = a % b
else:
    division = "Undefined (division by zero)"
    floor_division = "Undefined (division by zero)"
    modulus = "Undefined (division by zero)"

print(f"a + b = {addition}")
print(f"a - b = {subtraction}")
print(f"a * b = {multiplication}")
print(f"a / b = {division}")
print(f"a // b = {floor_division}")
print(f"a % b = {modulus}")
