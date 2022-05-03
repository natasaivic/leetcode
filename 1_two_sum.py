# 1. Two Sum

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order. 


def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result
    # return [i, j]


def twoSum_hash(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i 


nums = [2,7,11,15]
target = 9
twoSum_hash(nums, target)
