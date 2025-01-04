cities = ("Casablanca", "Rabat", "Marrakech", "Fès", "Tanger")

print("Second city:", cities[1])
print("Last city:", cities[-1])

new_cities = ("Agadir", "Oujda")
all_cities = cities + new_cities
print("All cities:", all_cities)

city_to_check = "Rabat"
print(f"Is {city_to_check} in tuple?", city_to_check in all_cities)
