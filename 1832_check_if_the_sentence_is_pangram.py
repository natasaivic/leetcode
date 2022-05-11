# 1832. Check if the Sentence Is Pangram 

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, 
# return true if sentence is a pangram, or false otherwise.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet. 


def checkIfPangram(sentence):
    pangram_set = set(sentence)
    pangram_set = "".join(sorted(pangram_set))
    return pangram_set == "abcdefghijklmnopqrstuvwxyz"
    