# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        temp = head
        while temp is not None:
            if temp in my_set:
                print("temp", temp)
                return True
            my_set.add(temp)
            temp = temp.next
        return False