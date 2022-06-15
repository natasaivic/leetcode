# 16. 3Sum Closest


# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


class Solution:
    def threeSumClosest(self, nums, target):
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    low += 1
                else:
                    high -= 1
            if diff == 0:
                break
        return target - diff