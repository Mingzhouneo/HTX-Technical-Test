
# HTX Technical Test

This repository contains solutions for the HTX xCode Technical Test (Backend Engineer).
This test includes:
1. A function to check if a string is a palindrome.
2. A function to check if an integer is a palindrome without converting it to a string
3. Unit tests for both implementations

## Project Structure
```
HTX-Technical-Test/
├── src/                 # Source code
│   ├── palindrome_string.py      # Palindrome check for strings
│   ├── palindrome_number.py      # Palindrome check for integers (without string conversion)
├── tests/               # Unit tests
│   ├── test_palindrome_string.py
│   ├── test_palindrome_number.py
├── .gitignore           # Files ignored by Git
├── README.md            # Project documentation
```

## How to Run
Ensure Python 3 is installed on your system.
Run the following commands to execute the scripts:

```
python src/palindrome_string.py
python src/palindrome_number.py
```
Example output:

```
'Was it a car or a cat I saw?' -> True
'Hello World' -> False
'!?' -> True

121 -> True
-121 -> False
10 -> False
```
## How to Run Tests
This project includes unit tests to verify the correctness of the implementations.
Run the tests using unittest:
```
python -m unittest discover tests
```
Expected output:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```
