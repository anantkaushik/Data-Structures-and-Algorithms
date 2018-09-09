import array
class myArray:
    def newArray(self, ar_type):
        self.arr = array.array(ar_type, []) # new array created
        
    def append(self,val):
        self.arr.append(val) # value added to the array
        return self.arr
        
    def insert(self,pos,val):
        self.arr.insert(pos,val) # value add at "pos" location
        return self.arr

    def pop(self):
        if len(self.arr)!=0:
            return self.arr.pop() # removing the last element
        return -1 # if array is empty

    def remove(self, val):
        if val in self.arr:
            self.arr.remove(val) # removing the first occurence of "val" 
        return self.arr

    def index(self, val):
        return self.arr.index(val) # finding the first index of "val"

    def reverse(self):
        self.arr.reverse() # reversing the array
        return self.arr