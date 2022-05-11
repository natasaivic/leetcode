# 459. Repeated Substring Pattern

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
# Example:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.


def repeatedSubstringPattern(s):
    return s in s[1:] + s[:-1]


# In the string "abab", we can see that the string can be splited into "ab" and "ab" to satisfy the result. 
# Instead of testing to find the substring that makes it valid, let's explore what we will get when we append two versions. 
# We get "abababab", which now has the substring "abab" in it 3 times. 
# (abab)abab
# abab(abab)
# ab(abab)ab
# The first two are not interesting because those will be true of every string we feed the algorithm. 
# The third ab(abab)ab is the key here.
# Now to see why we remove the first and last chars, lets look at a false result. aba. 
# When we duplicate the string, we get abaaba which again has (aba)aba and aba(aba) in it, but it does not have a third aba in the middle. 
# However return 'aba' in 'abaaba' would return true. By removing the first and last char, it becomes return 'aba' in 'baab' which is now false. 
# Back to the first example, it becomes return 'abab' in 'bababa' which works because of b(abab)a.