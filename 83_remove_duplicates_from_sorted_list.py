# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return
        
        current = head
        while current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next

        return head

# Complexity Analysis
# Time complexity: O(n). Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is O(n), where n is the number of nodes in the list.
# Space complexity: O(1). No additional space is used.
