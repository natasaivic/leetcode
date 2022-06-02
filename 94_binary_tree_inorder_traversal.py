# 94. Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Iterating method using Stack
class Solution:
    def inorderTraversal(self, root):
        stack = []
        depth_order = []
        
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif len(stack) > 0:
                root = stack.pop()
                depth_order.append(root.val)
                root = root.right
            else:
                break
        return depth_order

# Complexity Analysis
# Time complexity: O(n)
# Space complexity: O(n)
