# 21. Merge Two Sorted Lists


# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Q: We can't copy the values from the given lists into new list nodes to make our result list. 
# We have to take the nodes from provided lists and rearange them such that they point to each other. 

# Recursion
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # If one of them is empty, return the other one. 
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1 # once I know which head is smaller I can return it as head of the new list
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2 

# Whatever list has the smaller first element, will be returned at the end. (equal elements also satisfy)
# In the example l1 = [1,2,4] l2 = [1,3,4], we enter the if statement of line #24 first, this means that the first element of l1 doesn't get changed. 
# Next we move the pointer to the second element of l1 by calling the function again but with l1.next and l2 as input. 
# We call the function again, it goes to line #27 because now we have element 1 from l2 vs element 2 from l1. Now, l2 gets connected to the tail of l1. 
# We keep moving forward by switching between l1 and l2 until the last element. 


class Solution2:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
            
        head.next = self.mergeTwoLists(l1, l2)
        return head

# Complexity Analysis
# Time complexity : O(n + m)
# Space complexity : O(n + m) as we are calling mergeTwoLists(l1, l2) for evry single node in the list. 


# Iterative (Alternative solution that impruves space complexity. )

class Solution3:
    def mergeTwoLists(self, l1, l2):
        head = Node()
        tail = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1 != None:
            tail.next = l1
        else:
            tail.next = l2
        
        return head.next

# Complexity Analysis
# Time complexity : O(n + m)
# Space complexity : O(1)