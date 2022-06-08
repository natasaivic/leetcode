# 350. Intersection of Two Arrays II


# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


class Solution:
    def intersect(self, nums1, nums2):
        counts = {}
        result = []

        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for num in nums2:
            if num in counts:
                result.append(num)
                counts[num] -= 1
                if counts[num] == 0:
                    del counts[num]
                    

        return result