# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


def reverseString(s):

    head = 0
    tail = len(s) - 1

    while head < tail:
        temp = s[head]
        s[head] = s[tail]
        s[tail] = temp

        head = head + 1
        tail = tail + 1
