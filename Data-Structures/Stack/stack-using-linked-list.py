class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    
    def pop(self):
        if not self.head:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped
    
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

x = Stack() # Creating object of Stack class
x.push(1) # Pushing 1 to stack
x.push(2)  # Pushing 2 to stack
x.display() # 2 1
print(x.pop()) # Deleting the last element(2) from the stack.
x.display() # 1
print(x.pop()) # 1
print(x.pop()) # None(because stack is already empty)