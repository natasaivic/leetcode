# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node 
# down to the farthest leaf node.


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def maxDepthHelper(root):
    if root is None:
        return 0
    maxDepthLeft = maxDepthHelper(root.left)
    maxDepthRight = maxDepthHelper(root.right)
    return max(maxDepthLeft, maxDepthRight) + 1
    
class Solution:
    def maxDepth(self, root):
        depth = maxDepthHelper(root)
        return depth
        