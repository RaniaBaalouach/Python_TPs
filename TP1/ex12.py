def puissance(base, exponent):
    return base**exponent

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} to the power of {exponent} is: {puissance(base, exponent)}")
