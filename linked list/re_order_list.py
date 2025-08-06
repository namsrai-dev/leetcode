# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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


