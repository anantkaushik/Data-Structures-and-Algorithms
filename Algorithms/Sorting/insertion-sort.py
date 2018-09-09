"""
------------------------ INSERTION SORT -------------------------
Insertion sort works the way many people sort a hand of playing cards.
We start with an empty left hand and the cards face down on the table.
We then remove one card at a time from the table and insert it into the
correct position in the left hand. To find the correct position for a card,
we compare it with each of the cards already in the hand, from right to left.
At all times, the cards held in the left hand are sorted,
and these cards were originally the top cards of the pile on the table.
We present our pseudocode for insertion sort as a procedure called INSERTION- SORT,
which takes as a parameter an array A[1..n] containing a sequence of length n that is to be sorted.
The algorithm sorts the input numbers in place: it rearranges the numbers within the array A,
with at most a constant number of them stored outside the array at any time. The input array A
contains the sorted output sequence when the INSERTION-SORT procedure is finished.

Time Complexity:
Best Case: O(n)
Average Case: O(n*n)
Worst Case: O(n*n)
"""
def insertion_sort(arr):
	for i in range(0,len(arr)):
		temp = arr[i]
		j = i-1
		while j>=0 and arr[j]>temp:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = temp
	print ("Sorted array: ",arr)

arr = [2, 6, 1, 3, 4, 10]
insertion_sort(arr)