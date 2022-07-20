# 408. Valid Word Abbreviation 


class Solution:
    def validWordAbbreviation(self, word, abbr):
        i = len(word)
        j = len(abbr)
        m = 1
        prev = None
        
        while i > 0 and j > 0:
            c1, c2 = word[i-1], abbr[j-1]
            if c1 == c2:
                i -= 1
                j -= 1
                m = 1
                if prev == 0: return False
            elif c2.isnumeric():
                i -= int(c2)*m
                j -= 1
                m *= 10
                prev = int(c2)
            else: return False
        
        return i == j == 0