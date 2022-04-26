# 66. Plus One

# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


from unicodedata import digit


def plus_one(digits):
    return [int(i) for i in str(int(''.join(map(str, digits)) + 1))]
    

def plus_one_iterative(digits):

    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
            
    return [1] + digits

class Solution:
    def plus_one_recursive(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        
        else:
            digits = self.plusOne(digits[:-1]) + [0]
            return digits
            