# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


def longestCommonPrefix(strs):
    s = ""
    if len(strs) == 0:
        return s
    elif len(strs) == 1: 
        return strs[0]

    for a in range(len(min(strs))): 
        for b in range(1, len(strs)): 
            #compares nth character of first word to other words
            if strs[0][a] == strs[b][a]: 
                #only adds to pattern if nth character same up to the last word
                if b == len(strs)-1: 
                    s += strs[0][a]
            else: #exits when characters don't match
                return s
    return s
    