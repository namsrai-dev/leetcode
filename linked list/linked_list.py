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

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.print_list()