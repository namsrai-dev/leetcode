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
        while temp:
            temp = self.group_list(self, temp, k)

    def group_list(self, head):

        return None


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print_list()