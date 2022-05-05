# 314. Binary Tree Vertical Order Traversal

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. 
# (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.


from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Solution:
    def verticalOrder(root):
        columnTable = defaultdict(list)
        queue = []
        queue.append((root,0))

        while len(queue) > 0:
            node, column = queue.pop(0)
            if node is not None:
                columnTable[column].append(node.value)
            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

        result = []
        sortedColumnTable = sorted(columnTable.keys())
        for key in sortedColumnTable:
            result.append(columnTable[key])
            
        return result
