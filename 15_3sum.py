# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


def threeSum(nums):
    nums = sorted(nums)
    result = set()
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        target = 0 - nums[i]
        while l < r:
            if nums[l] + nums[r] == target:
                result.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return list(result)