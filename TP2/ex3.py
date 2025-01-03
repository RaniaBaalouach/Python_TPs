people = {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40, "Eve": 45}

people["Frank"] = 50
print("After adding:", people)

people.pop("Charlie")
print("After removal:", people)

print("Names:", list(people.keys()))

print("Ages:", list(people.values()))
