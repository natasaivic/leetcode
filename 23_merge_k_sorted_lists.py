# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        
class Solution:
    def mergeKLists(lists):
        if lists is None: 
            return 
        result = []
        for i in lists:
            current = i
            while current is not None:
                result.append(current.val)
                current = current.next
        
        if result is None: 
            return
        result.sort()
        head = ListNode()
        m=head
        for k in result:
            m.next = ListNode(k)
            m = m.next
        return head.next
