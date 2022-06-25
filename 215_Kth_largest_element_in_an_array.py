# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]