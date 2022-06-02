# 700. Search in a Binary Search Tree

# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree 
# rooted with that node. If such a node does not exist, return null.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        if root is None:
            return
        
        if root.value == val:
            return root
        
        if val > root.value:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)