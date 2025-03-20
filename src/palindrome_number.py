def is_palindrome_number(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):  # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10

if __name__ == "__main__":
    test_cases = [121, -121, 10]
    for test in test_cases:
        print(f"{test} -> {is_palindrome_number(test)}")
