class Stack:
    arr = []
    def push(self,item):
        self.arr.append(item)
    
    def spop(self):
        if len(self.arr) > 0:
            return self.arr.pop()
        else:
            return #stack is empty
    
    def display(self):
        print(self.arr)

x = Stack() # Creating object of Stack class
x.push(1) # Pushing 1 to stack
x.push(2)  # Pushing 2 to stack
x.display() # arr = [1,2]
x.spop() # Deleting the last element from the stack.
x.display() # arr = [1]
print(x.spop()) # 1
print(x.spop()) # None(because stack is already empty)