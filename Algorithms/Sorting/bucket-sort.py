"""
Bucket sort is a comparison sort algorithm that operates on elements by dividing them 
into different buckets and then sorting these buckets individually. Each bucket is 
sorted individually using a separate sorting algorithm or by applying the bucket 
sort algorithm recursively. Bucket sort is mainly useful when the input is uniformly 
distributed over a range.

Average & Best Case Time Complexity: O(n+k)
Worst Case Time Complexity: O(n*n) 

Space complexity: O(n+k).
"""

import math
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        temp = arr[i] 
        j = i - 1
        while j >=0 and arr[j] > temp:  
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = temp      
    return arr    

def bucketSort(arr):
    buckets = [[] for _ in range(len(arr))] # Creating Buckets
    divider = math.ceil((max(max(arr), len(arr))+1)/len(buckets)) 
    # Adding numbers in buckets
    for i in arr:
        j = i//divider
        buckets[j].append(i)
    # Sorting the buckers
    for i in range(len(buckets)):
        buckets[i] = insertionSort(buckets[i])
    
    # Merging Buckets
    k = 0
    for i in range(len(buckets)): 
        for j in range(len(buckets[i])): 
            arr[k] = buckets[i][j] 
            k += 1
    
arr = [10,9,8,7]
bucketSort(arr)
print(arr)