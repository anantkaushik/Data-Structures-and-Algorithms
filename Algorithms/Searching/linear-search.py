"""
Problem Statement:

Given a list of n elements with values and target element, find the index/position of the target in list.

The linear search is a basic search algorithm which searches all the elements in the list and finds the required value. 
This is also known as sequential search.

Time Complexity:

Best Case: O(1)
Average Case: O(n)
Worst Case: O(n)
"""
def linearSearch(arr,target):
    for i in range(len(arr)): # traversing the list
        if arr[i] == target: # comparing the list element with the target value
            return i # return the index if list element is equal to the target element
    return -1 # if target is not present in the list it will return -1

a = [1,2,4,5,8]
print(linearSearch(a,5)) # it will return 3 as 5 is present at 3rd index
print(linearSearch(a,9)) # it will return -1 since 9 is not present in the list