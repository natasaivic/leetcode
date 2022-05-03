# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


def validPalindrome(self, s: str) -> bool:
    h = 0
    t = len(s) - 1 
    while h < t:
        if s[h] != s[t]:  # delete s[h] or s[t] and validate palindrome finally
                return s[h:t] == s[h:t][::-1] or s[h + 1:t + 1] == s[h + 1:t + 1][::-1]
        h = h + 1 
        t = t - 1
    return True
    