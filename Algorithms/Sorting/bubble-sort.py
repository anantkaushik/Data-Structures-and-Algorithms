"""
Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without 
any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
# Worst and Average Case Time Complexity: O(n*n).
# Best Case Time Complexity: O(n*n).

def optimizedBubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]: # Swap if the element found is greater than the next element.
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if swap == False: # IF no two elements were swapped by inner loop, then break. (It is the case when the array is already sorted)
            break
    return arr
# Worst and Average Case Time Complexity: O(n*n). 
# Best Case Time Complexity: O(n).

a = [1,2,4,5,8]
print(*bubbleSort(a))
print(*optimizedBubbleSort(a))