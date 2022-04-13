# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. 
# # Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.


def singleNumber(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        for key, value in counts.items():
            if value == 1:
                return key