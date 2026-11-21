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
            temp.next = ListNode(i + 2)
            temp = temp.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        group_tail = dummy      # өмнөх бүлгийн сүүл
        prev = None
        old_head = None
        temp = head
        count = 1

        while temp:
            if count == 1:
                old_head = temp
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

            if count == k:
                group_tail.next = prev   # өмнөх сүүл -> энэ бүлгийн шинэ толгой
                group_tail = old_head    # энэ бүлгийн сүүл дараагийн холбох цэг
                prev = None
                count = 1
            else:
                count += 1

        # k-д хүрээгүй үлдэгдэл prev дотор урвуу байгаа тул буцааж эргүүлнэ
        rest = None
        while prev:
            nxt = prev.next
            prev.next = rest
            rest = prev
            prev = nxt
        group_tail.next = rest

        return dummy.next

    def printList(self, head):
        vals = []
        while head:
            vals.append(str(head.val))
            head = head.next
        print(" -> ".join(vals))


sol = Solution()
sol.printList(sol.reverseKGroup(sol.head, 3))
# 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7