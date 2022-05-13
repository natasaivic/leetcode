# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        
        prev = None
        current = head
        while current is not None:
            #assign the value of head to the temp variable
            temp = current 
            current = current.next
            temp.next = prev
            prev = temp
        return prev
        