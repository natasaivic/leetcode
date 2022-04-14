# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


def anagram(s, t):
    dictionary = {}

    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    for i in t:
        if i in dictionary:
            dictionary[i] -= 1
        else:
            return False
    
    for key, value in dictionary.items():
        if value != 0:
            return False
    
    return True


def anagram_2(s, t):
    sortedString_s = ''.join(sorted(s))
    sortedString_t = ''.join(sorted(t))
    
    return sortedString_s == sortedString_t