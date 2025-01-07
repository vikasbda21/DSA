class Node:
    def __init__(self, data=None):
        self.data = data  # The value stored in that node
        self.next = None  # Pointer to the next value


class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        current = self.head
        if not current:
            print("The linked list is empty.")
            


ll = LinkedList()


ll.display()