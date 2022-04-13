# 2053. Kth Distinct String in an Array

# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
# If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.


def kthDistinct(arr, k):
    n = len(arr)
    dictionary = {}
    for i in arr:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    distinct = []
    for i in range(n):
        if dictionary[arr[i]] == 1:
            distinct.append(arr[i])
    
    if len(distinct) < k:
        return ""
    else:
        return distinct[k-1]