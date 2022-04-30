# 9. Palindrome Number

# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


def isPalindrome(x):
    temp = x
    reverse = 0
    while temp > 0:
        reverse = reverse * 10 + (temp % 10 )
        temp = temp // 10
    
    return x == reverse
