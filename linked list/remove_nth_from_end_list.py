# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode()
        temp = start
        temp.next = head
        prev = temp
        cnt = 0
        while temp:
            if cnt > n:
                prev = prev.next
                print("prevs", prev.val)
                # prev = prev.next
            temp = temp.next
            cnt += 1
        if prev:
            print("prev", prev.val)
        if prev.next:
            print("prev.next", prev.next.val)
            prev.next = prev.next.next
        print("head", head.val)
        return start.next
