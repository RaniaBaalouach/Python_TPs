people = {"Ahmed": 25, "Fatima": 30, "Youssef": 35, "Imane": 40, "Hassan": 45}

people["Khadija"] = 50
print("After adding:", people)

people.pop("Youssef")
print("After removal:", people)

print("Names:", list(people.keys()))

print("Ages:", list(people.values()))
