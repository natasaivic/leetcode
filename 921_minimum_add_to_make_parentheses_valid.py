# 921. Minimum Add to Make Parentheses Valid


# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.


def minAddToMakeValid(s):
    opening = 0
    count = 0
    for i in s:
        if i == '(': 
            opening += 1
        else:
            if opening > 0: 
                opening -= 1
            else: 
                count += 1
    return count + opening