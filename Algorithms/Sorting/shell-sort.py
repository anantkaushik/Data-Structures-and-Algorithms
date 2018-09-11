"""
------------------------ SHELL SORT -------------------------
ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. 
When an element has to be moved far ahead, many movements are involved. The idea of shellSort is to allow exchange of far items. 
In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. 
An array is said to be h-sorted if all sublists of every h’th element is sorted.

Time Complexity:  O(n**3/2)
"""
def shell_sort(arr):
    n = len(arr)
    h = 1
    while h<(n//3):
        h= 3 * h + 1
    while h >=1:
        for i in range(h,n):
            temp = arr[i]
            j = i
            while j>=h and arr[j-h]>temp:
                arr[j] = arr[j-h]
                j-=h
            arr[j] = temp
        h = h//3
    print ("Sorted array: ",arr)
        
arr = [2, 6, 1, 3, 4, 10]
shell_sort(arr) 