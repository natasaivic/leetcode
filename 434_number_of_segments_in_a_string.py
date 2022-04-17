# 434. Number of Segments in a String

# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.


def countSegments(s):
    words = 0
    count = True

    for i in range(0, len(s)):
        if s[i] != " " and count == True:
            words += 1
            count = False
        elif s[i] == " ":
            count = True

    return words
    