class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print("new_node -> ", temp.val)
            temp = temp.next

    
    def merge_group(self, k):
        temp = self.head
        temp_head = None
        temp_tail = None
        while temp:
            new_head, new_tail, next = self.group_list(temp, k)
            if not temp_head:
                temp_head = new_head
            else:
                temp_tail.next = new_head
            temp_tail = new_tail
            temp = next

        self.head = temp_head

    def group_list(self, head, k):
        cnt = 1
        temp = head
        while temp and cnt < k:
            cnt += 1
            temp = temp.next

        print("head value =>", head.val)
        print("tail value =>", temp.val if temp else None)
        print("tail next =>", temp.next if temp and temp.next else None)
        print("cnt == k ------------- ", cnt, k)
        if cnt == k and temp:
            next = temp.next if temp and temp.next else None
            if temp and temp.next:
                temp.next = None
            new_head, new_tail = self.revese_list(head, k)
            return new_head, new_tail, next
        else:
            return head, None, None

    def revese_list(self, head, k):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev, head



        # return temp


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print_list()

my_list.merge_group(3)

my_list.print_list()
