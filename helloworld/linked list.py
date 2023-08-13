class node:
# Represent a node of the singly linked listclass Node:
    def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
# Represent the head and tail of the singly linked list
    def __init__(self):
        self.head = None
        self.tail = None
# add_node() will add a new node to the list
    def add_node(self, data):
# Create a new node
        new_node = Node(data)
# Checks if the list is empty
        if self.head == None:
# If list is empty, both head and tail will point to new node
            self.head = new_node
            self.tail = new_node
        else:
# new_node will be added after tail such that tail's next will point to new_node
            self.tail.next = new_node
# newNode will become new tail of the list
            self.tail = new_node
# removeDuplicate() will remove duplicate nodes from the list
    def remove_duplicate(self):
# Node current will point to head
        current = self.head
        index = None
        temp = None
        if self.head == None:
            return
        else:
            while current != None:
# Node temp will point to previous node to index.
                temp = current
# Index will point to node next to current
                index = current.next
            while index != None: