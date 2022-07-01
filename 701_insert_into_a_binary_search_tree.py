# 701. Insert into a Binary Search Tree


# You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
# Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, 
# as long as the tree remains a BST after insertion. You can return any of them.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Solution:
    def insertIntoBST(self, root, value):
        if root is None:
            return Node(value)

        if root.value == value:
            return root

        if value > root.value:
            root.right = self.insertIntoBST(root.right, value)
        else:
            root.left = self.insertIntoBST(root.left, value)
        return root