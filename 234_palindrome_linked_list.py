# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome.


class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

# Copy into array and then use two pointer technique
class Solution:
    def isPalindrome(self, head):
        arr = []
        current = head
        while current is not None:
            arr.append(current.value) 
            current = current.next
        
        current = head
        while current is not None:
            if current.value != arr.pop():
                return False
            current = current.next
        return True

# Complexity Analysis
# Time complexity: O(n)
# Space complexity: O(n)

# Improve space complexity
# Reverse Second Half In-place
