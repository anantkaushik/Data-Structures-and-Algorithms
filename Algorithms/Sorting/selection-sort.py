"""
Selection sort: 
One of the simplest sorting algorithms works as follows: First, find
the smallest item in the array and exchange it with the first entry (itself if the first entry
is already the smallest). Then, find the next smallest item and exchange it with the sec-
ond entry. Continue in this way until the entire array is sorted. This method is called
selection sort because it works by repeatedly selecting the smallest remaining item.
Running time is insensitive to input. 
The process of finding the smallest item on one
pass through the array does not give much information about where the smallest item
might be on the next pass. This property can be disadvantageous in some situations.
For example, the person using the sort client might be surprised to realize that it takes
about as long to run selection sort for an array that is already in order or for an array
with all keys equal as it does for a randomly-ordered array! As we shall see, other algo-
rithms are better able to take advantage of initial order in the input.
Data movement is minimal. 
Each of the N exchanges changes the value of two array
entries, so selection sort uses N exchanges—the number of array accesses is a linear
function of the array size. None of the other sorting algorithms that we consider have
this property (most involve linearithmic or quadratic growth).

Time Complexity:
Best Case: O(n*n)
Average Case: O(n*n)
Worst Case: O(n*n)
"""

class selection_sort:
    def selectionSort(self,arr):
        for i in range(len(arr)-1):
            minn = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[minn]:
                    minn = j #finding the minimum element
            arr[i],arr[minn] = arr[minn],arr[i] #swapping the minimum element with the first element
        return arr
        
s = selection_sort()
arr = [1,2,7,5,3,6,0]
print(s.selectionSort(arr))