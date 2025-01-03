def count_occurrences(lst, value):
    return lst.count(value)

lst = input("Enter a list of values (comma-separated): ").split(',')
value = input("Enter a value to count: ")
print(f"Occurrences of '{value}': {count_occurrences(lst, value)}")
