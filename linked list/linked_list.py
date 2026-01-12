class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def pop(self):
        if self.head is None:
            return None
        
        if not self.head.next:
            pop_value = self.head.value
            self.head = None
            return pop_value
        
        cur = self.head
        while cur.next.next:
            cur = cur.next

        pop_value = cur.next.value
        cur.next = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def reverse_list(self):
        # prev, curr = None, self.head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # self.head = prev
        # return prev
        prev = None
        curr = self.head
        while curr:
            print("-", curr.value)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        self.head = prev


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.reverse_list()
# linked_list.pop()
# linked_list.print_list()z
# print(linked_list.reverse_list())
linked_list.print_list()