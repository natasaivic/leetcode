# 543. Diameter of Binary Tree


# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0
        def height(root):
            nonlocal diameter
            if root is None:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        height(root)
        return diameter

        