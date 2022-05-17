# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.

# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. 


def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    
    seen = {}
    left, right = 0, 0
    longest = 1
    while right < len(s):
        if s[right] in seen:
            left = max(left,seen[s[right]]+1)
        longest = max(longest, right - left + 1)
        seen[s[right]] = right
        right += 1
        print(left, right, longest)
    return longest
    