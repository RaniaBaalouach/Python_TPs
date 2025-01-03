def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")
