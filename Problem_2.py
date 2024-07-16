import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFD', input_str)
    return ''.join([char for char in nfkd_form if not unicodedata.combining(char)])

def is_palindrome(s):
    filtered_chars = ''.join(remove_accents(char).lower() for char in s if char.isalnum())
    return filtered_chars == filtered_chars[::-1]

if __name__ == "__main__":
    test_string = input("Enter a string: ")
    print(f"Is palindrome: {is_palindrome(test_string)}")
