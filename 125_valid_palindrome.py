# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


def validPalindrome(s):

    new_string = ""
    s = s.lower()
    for i in s:
        if i.isalnum():
            new_string.append(i)
    
    return new_string == new_string[::-1]
