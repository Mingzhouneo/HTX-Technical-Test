import re

def is_palindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())  # Remove non-alphanumeric characters
    return s == s[::-1]  # Check if it reads the same forward and backward

if __name__ == "__main__":
    test_cases = ["Was it a car or a cat I saw?", "Hello World", "!?"]
    for test in test_cases:
        print(f"'{test}' -> {is_palindrome(test)}")
