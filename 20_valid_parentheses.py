# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order. 


def validParentheses(s):
    stack = []
    dictionary = {'(' : ')', '{' : '}', '[' : ']'}
    
    for i in s:
        # if i is the left bracket then we append it to the stack
        if i in dictionary: 
            stack.append(i)
        # else if i is the right bracket and 
        # the stack is empty (meaning no matching left bracket) or the left bracket doesn't match
        elif len(stack) == 0 or dictionary[stack.pop()] != i:
            return False
    
    # check if the stack still contains unmatched left bracket
    return len(stack) == 0 
