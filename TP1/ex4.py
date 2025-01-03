# File: math_operations.py

import math

a = float(input("Enter number A: "))
b = float(input("Enter number B: "))

square_a = a**2
square_b = b**2
power_ab = a**b

tangent_a = math.sin(a) / math.cos(a) if math.cos(a) != 0 else "Undefined (cos(A) is zero)"

print(f"The square of A: {square_a}")
print(f"The square of B: {square_b}")
print(f"A to the power B: {power_ab}")
print(f"The tangent of A: {tangent_a}")
