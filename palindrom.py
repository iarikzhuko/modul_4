def is_palindrome(s):
    A = [a.lower() for a in s if a.isalpha()]
    if A==A[::-1]:
        return True
    else:
        return False

print(is_palindrome("мадам"))# для примера
 