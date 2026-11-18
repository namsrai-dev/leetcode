# LRU Cache
# Medium
# Topics
# Company Tags
# Hints
# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in 
# O
# (
# 1
# )
# O(1) average time complexity.

# Example 1:

# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20 
# lRUCache.get(1);      // return -1 (not found)

class ListNode:
    def __init__(self, k, v):
        self.prev = self.next = None
        self.key = k
        self.val = v

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_dict = {}
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.right

    def remove(self, node):
        pass

    def insert(self, node):
        pass


    def get(self, key: int) -> int:
        pass
        
    def put(self, key: int, value: int) -> None:
        pass
