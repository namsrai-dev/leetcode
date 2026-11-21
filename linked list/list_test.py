from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
        self.head = ListNode(1)
        temp = self.head
        for i in range(6):
            print(i)
            temp.next = ListNode(i+2)
            temp = temp.next

        temp2 = self.head
        while temp2:
            print("list", temp2.val)
            temp2 = temp2.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

sol = Solution()