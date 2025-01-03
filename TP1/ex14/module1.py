def is_palindrome(word):
    return word == word[::-1]

def count_occurrences(lst, value):
    return lst.count(value)

def table_multiplication(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
