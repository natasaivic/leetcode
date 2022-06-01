# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome.


class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

class Solution:
    def isPalindrome(self, head):
        stack = []
        current = head
        while current is not None:
            stack.append(current.value) 
            current = current.next
        
        current = head
        while current is not None:
            if current.value != stack.pop():
                return False
            current = current.next
        return True