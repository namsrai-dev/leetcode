# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:

# [0, 1, 2, 3, 4, 5, 6]

# [0, 6, 1, 5, 2, 4, 3]

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        new_node = demo = ListNode()
        while temp:
            print("temp.val", temp.val)
            new_node.next = ListNode(temp.val)
            temp = temp.next

            cur = temp
            prev = None
            while cur:
                prev = cur
                cur = cur.next
            if prev:
                print("prev.val", prev.val)
                new_node.next = ListNode(prev.val)
        self.head = demo.next

        while new_node:
            print(new_node.val)
            new_node = new_node.next



sol = Solution()
sol.reorderList()
