def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a text: ").replace(" ", "")

print(f"The text '{word}' is {'a palindrome' if is_palindrome(word) else 'not a palindrome'}.")