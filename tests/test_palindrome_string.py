import unittest
from src.palindrome_string import is_palindrome

class TestPalindromeString(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
    
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Hello World"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome("!?"))

if __name__ == '__main__':
    unittest.main()
