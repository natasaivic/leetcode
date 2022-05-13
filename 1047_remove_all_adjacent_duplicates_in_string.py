# 1047. Remove All Adjacent Duplicates In String

# You are given a string s consisting of lowercase English letters. 
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. 
# It can be proven that the answer is unique.


def removeDuplicates(s) -> str:
    output = []
    for ch in s:
        if output and ch == output[-1]: 
            output.pop()
        else: 
            output.append(ch)
    return ''.join(output)