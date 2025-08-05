class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        return
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print("val ->", temp.value)
            temp = temp.next


def merge_two_list(list1: LinkedList, list2: LinkedList):
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

# def append

        
    
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(2)
list1.append(3)
list1.print_list()

list2 = LinkedList()
list2.append(0)
list2.append(1)
list2.append(1)
list2.append(5)
list2.print_list()