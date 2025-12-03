class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = Node(val)

    def print_list(self):
        temp = self.head
        while temp is not None:
            temp = temp.next

    
linked_list = LinkedList()
linked_list.append(0)
linked_list.append(1)
linked_list.append(2)
linked_list.print_list()