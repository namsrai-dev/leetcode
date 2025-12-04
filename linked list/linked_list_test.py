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
            print(temp.val)
            temp = temp.next


    def reverse_linked_list(self):
        prev = None
        curr = self.head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev

            prev = curr
            curr = nextNode

        self.head = prev


    # def reverse_linked_list(self):
    #     prev = None
    #     curr = self.head

    #     while curr is not None:
    #         nextNode = curr.next
    #         curr.next = prev

    #         prev = curr
    #         curr = nextNode

    #     self.head = prev

    
linked_list = LinkedList()
linked_list.append(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.print_list()
linked_list.reverse_linked_list()
linked_list.print_list()