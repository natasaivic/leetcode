# 98. Validate Binary Search Tree


# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

import math
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self, root):
        def is_bst_helper(node, low=-math.inf, high=math.inf):
            if node is None:
                return True
            if node.val < low or node.val > high:
                return False
            return is_bst_helper(node.left, low, node.val - 1) and is_bst_helper(node.right, node.val + 1, high)

        return is_bst_helper(root)
   