# 203. Remove Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class Solution:
    def removeElements(self, head, val):
        if head is None:
            return None
        
        while head.value == val:
            head = head.next
            if head is None:
                return
        
        current = head
        while current.next is not None:
            if current.next.value == val:
                current.next = current.next.next
                continue
            # else:
            current = current.next
            
        return head
