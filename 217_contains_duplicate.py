# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


def containsDuplicate(nums):
    numsSet = set(nums)
    if len(nums) == len(numsSet):
        return False
    return True
    