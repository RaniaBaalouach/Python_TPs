from ex14.module1 import is_palindrome, count_occurrences, table_multiplication
from ex14.module2 import puissance, is_leap_year

print("Testing module1:")
print(f"Is 'radar' a palindrome? {is_palindrome('radar')}")
print(f"Occurrences of 1 in [1, 2, 3, 4, 1, 2, 1]: {count_occurrences([1, 2, 3, 4, 1, 2, 1], 1)}")
table_multiplication(5)

print("\nTesting module2:")
print(f"2 to the power 3 is: {puissance(2, 3)}")
print(f"Is 2024 a leap year? {is_leap_year(2024)}")
