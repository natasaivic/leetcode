# 146. LRU Cache


# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


# Resoning: 
# Implement the structure which provides the following operations in O(1) time:
# Get the key, first check if the key exists
# Put the key, but first delete the first added key

# First intuition: OrderedDict()
# The only difference between dict() and OrderedDict() is that: 
# OrderedDict preserves the order in which the keys are inserted. In the dict, the ordering may or may not be happen.
# The only problem here is space complexity : O(capacity) 

# Second intuition: 
# The problem can be solved with a hashmap that keeps track of the keys and 
# its values in the double linked list. 
# That results in O(1) time for put and get operations and allows to remove the first added node in O(1) time as well.

# One advantage of double linked list is that the node can remove itself without other reference. 
# In addition, it takes constant time to add and remove nodes from the head or tail.

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)