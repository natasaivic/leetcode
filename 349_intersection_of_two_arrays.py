# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.


def intersectionOfTwoArrays(nums1, nums2):

    dictionary = {}
    result = []

    for num in nums1:
        if num in nums2:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
    
    for key, value in dictionary.items():
        result.append(key)
    
    return result


def intersectionOfTwoArrays_2(nums1, nums2):

    intersection = set()
    for num in nums1:
        if num in nums2:
            intersection.add(num)

    return intersection
