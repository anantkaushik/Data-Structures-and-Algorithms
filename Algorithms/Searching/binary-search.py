"""
Binary search is the most popular Search algorithm.It is efficient and also one of the most commonly used techniques 
that is used to solve problems.
Binary search works only on a sorted set of elements. To use binary search on a collection, the collection must first be sorted.

Binary search looks for a particular item by comparing the middle most item of the collection. If a match occurs, 
then the index of item is returned. If the middle item is greater than the item, then the item is searched in the sub-array 
to the left of the middle item. Otherwise, the item is searched for in the sub-array to the right of the middle item. 
This process continues on the sub-array as well until the size of the subarray reduces to zero.

Time Complexity:

Best Case O(1)
Average Case O(log n)
Worst Case O(log n)
"""

def binarySearch(arr,target):
    l = len(arr) - 1
    start,end = 0,l 
    mid = (start+end)//2 
    while start <= end:
        if arr[mid] == target: 
            return mid 
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start+end)//2
    return -1
    
a = [1,2,4,5,8]
print(binarySearch(a,5)) # it will return 3 as 5 is present at 3rd index
print(binarySearch(a,9)) # it will return -1 since 9 is not present in the list