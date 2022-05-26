# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution1:
    def removeNthFromEnd(self, head, n):
        length = 0
        first = head
        while first is not None:
            first = first.next
            length += 1

        second = head
        # edge case: if we have to delete head node (i.e: length == n)
        if length == n:
            head = head.next

        else:
            index_to_remove = length - n
            while index_to_remove > 1:
                second = second.next
                index_to_remove -= 1

            second.next = second.next.next
        return head

#      s   f We want to stop right before the node that we want to remove. 
# [1,2,3,4,5]
class Solution2:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
            
        if fast is None:
            return head.next
        
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return head
