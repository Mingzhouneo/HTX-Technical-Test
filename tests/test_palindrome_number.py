import unittest
from src.palindrome_number import is_palindrome_number

class TestPalindromeNumber(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome_number(121))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome_number(-121))
        self.assertFalse(is_palindrome_number(10))

if __name__ == '__main__':
    unittest.main()
