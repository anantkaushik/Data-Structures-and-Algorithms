"""
Priority Queue:
       Priority Queue is an extension of queue with following properties.
           1) Every item has a priority associated with it.
           2) An element with high priority is dequeued before an element with low priority.
           3) If two elements have the same priority, they are served according to their order in the queue.
 
       A typical priority queue supports following operations.
           ➤ insert(item, priority): Inserts an item with given priority.
           ➤ getHighestPriority(): Returns the highest priority item.
           ➤ deleteHighestPriority(): Removes the highest priority item.
 
       Applications of Priority Queue:
           1) CPU Scheduling
           2) Graph algorithms like Dijkstra’s shortest path algorithm, Prim’s Minimum Spanning Tree, etc
           3) All queue applications where priority is involved.
           4) Data Compression (Huffman codes)
           5) Find the largest M items in a stream of N items.
 
       Ways to implement Priority Queue
           ➤ Arrays - Insertion and Deletion is expensive in order to maintain the priority.
           ➤ LinkedList -> Same as array. But deletion is fast.
           ➤ Binary Heap -> Best

 Binary Heap (Min Heap or Max Heap)
       Based on the idea of Complete Binary Tree.
       Binary Tree -> Empty or Nodes to left and right binary tree.
       Complete Binary Tree -> Perfectly Balanced, except for the bottom level and the bottom level has all keys as left as possible.
 
                           o                   <- Level 0
                        /     \
                       o       o               <- Level 1
                     /  \     /  \
                    o    o   o    o            <- Level 2
                   / \
                  o   o                        <- Level 3
 
             ✔︎ Perfectly Balanced, except for Level 3
             ✔︎ Height of a Complete Binary Tree of N node is Log N.
                   In above tree, there are 9 nodes ==> Log 9 = Log 3^2 = 2 Log 3. (3 Levels)
 
 
       Implementation - Array representation of the heap ordered complete binary tree.
       Head Ordered Binary Tree:
           ✬  Keys in nodes.
           ✬  Parent's key is smaller than children's keys. This is important. ✅
 
       Properties of Binary Heap:
           ➤ Smallest key is arr[1], which is the root of the binary tree.
           ➤ Parent of node at 'k' index is at k/2 index. (It's integer divide. No floats)
           ➤ Children of a node 'k' are at index '2k' and '2k + 1', given we start indexing from 1 instead of 0. ✅
        We don't need actual tree to represent these data structures. Array indices are sufficient.
 
Time complexity for Building a Binary Heap is O(N).
"""
# This is the example Min Heap
class binHeap:
    def __init__(self):
        self.heapList = [0]
        self.curSize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2
    
    def insert(self, n):
        self.heapList.append(n)
        self.curSize += 1
        self.percUp(self.curSize)
        
    def percDown(self, i):
        while i * 2 <= self.curSize:
            minn = self.minChild(i)
            if self.heapList[i] > self.heapList[minn]:
                self.heapList[i], self.heapList[minn] = self.heapList[minn], self.heapList[i]
            i = minn
    
    def minChild(self, i):
        if (i * 2) + 1 > self.curSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            return i * 2 + 1
            
    def delMin(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.curSize]
        self.curSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return val
        
    def buildHeap(self, alist):
        i = len(alist)//2
        self.curSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
            
    def getMin(self):
        return self.heapList[1]
            
x = binHeap()
x.buildHeap([9, 6, 5, 2, 3])
print(x.heapList) # Print [0, 2, 3, 5, 6, 9]
print(x.delMin()) # Print 2
print(x.heapList) # Print [0, 3, 6, 5, 9]
x.insert(2)
print(x.heapList) # Print [0, 2, 3, 5, 9, 6]
print(x.getMin()) # Print 2