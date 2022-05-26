# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# To detect if a list is cyclic, we can check whether a node had been visited before. 
class Slution1:
    def hasCycle(head):
        visited_nodes = set()
        while head is not None:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False

# Complexity analysis
# Time complexity : O(n).
# Space complexity : O(n). 


# Improving space complexity:
# Imagine two runners running on a track at different speed. What happens when the track is actually a circle?
# The slow pointer moves one step at a time while the fast pointer moves two steps at a time.
class Solution2:
    def hasCycle(head):
        if head is None:
            return
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None: #Ako jedan izadje iz liste nema cycle. 
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True

# Complexity analysis
# Time complexity : O(n). 
# List has no cycle: The fast pointer reaches the end first and the run time depends on the list's length, which is O(n).
# List has a cycle: O(n)
# Space complexity : O(1). We only use two nodes (slow and fast) so the space complexity is O(1).
