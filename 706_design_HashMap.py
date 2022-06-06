# 706. Design HashMap


# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. 
# If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self):
        self.bucket = [None] * 1000
        
    def put(self, key, value):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            self.bucket[index] = Item(key, value)
            return

        current = self.bucket[index]
        last = current
        while current is not None:
            if current.key == key:
                current.value = value
                return True
            last = current
            current = current.next
        
        last.next = Item(key, value)

    def get(self, key):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            return -1
    
        current = self.bucket[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            return False

        if self.bucket[index].key == key:
            self.bucket[index] = self.bucket[index].next
            return True

        previous = self.bucket[index]
        current = self.bucket[index].next
        while current is not None:
            if current.key == key:
                previous.next = current.next
                return True
            previous = current
            current = current.next
        return False
       