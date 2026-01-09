class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = ListNode(0,0)
        self.left = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        return -1

    def delete_node(self):
        to_delete = self.right.prev
        prev = self.right.prev.prev
        prev.next = self.right
        self.right.prev = prev
        # next = self.right.next.next
        # prev.next = next
        # next.prev = prev
        print("to_delete.key", to_delete.key)
        print("self.cache[to_delete.key]", self.cache[to_delete.key])
        del self.cache[to_delete.key]


    def print_list(self):
        temp = self.left
        while temp:
            print(temp.key, temp.val)
            temp = temp.next


    def put(self, key: int, value: int) -> None:
        new_node = ListNode(key, value)
        next = self.left.next
        # prev = self.left.next.prev
        self.left.next = new_node
        new_node.prev = self.left
        new_node.next = next
        next.prev = new_node

        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            self.delete_node()



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.put(4,4)
obj.put(3,3)
obj.print_list()
# param_1 = obj.get(key)
# obj.put(key,value)