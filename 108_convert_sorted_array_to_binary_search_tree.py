# 108. Convert Sorted Array to Binary Search Tree


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class Solution:
    def sortedArrayToBST(self, nums):
        if nums == []:
            return None

        mid = len(nums) // 2

        root = Node(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root