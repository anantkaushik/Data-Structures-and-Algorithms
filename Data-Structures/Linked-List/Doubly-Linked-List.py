"""
------------------------ Doubly Linked List -------------------------
"""
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def get(self, index):
        if index >= self.length():
            return "ERROR : index out of range!"
        idx = 0
        cur = self.head
        while cur:
            if idx == index:
                return cur
            idx += 1
            cur = cur.next
    
    def insertAtBeg(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = self.tail = newNode
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.tail:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            self.head = self.tail = newNode
    
    def insertAfter(self, refNode, data):
        if not refNode: #if reference node does not exist
            return
        newNode = Node(data)
        newNode.prev = refNode
        if refNode.next is None:
            self.tail = newNode
        else:
            newNode.next = refNode.next
            newNode.next.prev = newNode
        refNode.next = newNode

    def insertBefore(self, refNode, data):
        if not refNode: #if reference node does not exist
            return
        newNode = Node(data)
        newNode.next = refNode
        if refNode.prev is None:
            self.head = newNode
        else:
            newNode.prev = refNode.prev
            refNode.prev.next = newNode
        refNode.prev = newNode

    def remove(self, node):
        if not node: #if reference node does not exist
            return
        if not node.prev:
            self.head = node.next
        else:
            node.prev.next = node.next
        if not node.next:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
    
    def display(self):
        elements = []
        cur = self.head
        while cur:
            elements.append(cur.data)
            cur = cur.next
        return elements

x = doublyLinkedList() # creating object of doublyLinkedList
x.insertAtBeg(1) # Inserting 1 at the begining
x.insertAtEnd(2) # Inserting 2 at the end
x.insertAtEnd(6) # Inserting 6 at the end
x.insertAfter(x.get(1),5) # Inserting 5 after 1st(according to index) node
x.insertBefore(x.get(3),10)# Inserting 10 before 3rd(according to index) node
x.remove(x.get(1)) # Removing 1st(according to index) node
print(x.length()) # Print the length of the Linked List
print(x.display()) # Print the Linked List i.e. [1,5,10,6]