# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid+1
            else:
                if nums[mid] == target and nums[mid-1] != target:
                    return mid
                else:
                    r = mid-1
        return l