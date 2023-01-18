# Python3 program for the above approach

# importing heapq module
# to implement heap
import heapq as hq


def FirstKelements(arr, size, k):
    # Creating Min Heap for given
    # array with only k elements
    # Create min heap using heapq module
    minHeap = []

    for i in range(k):
        minHeap.append(arr[i])
    hq.heapify(minHeap)
    # Loop For each element in array
    # after the kth element

    for i in range(k, size):
        # If current element is smaller
        # than minimum ((top element of
        # the minHeap) element, do nothing
        # and continue to next element

        if minHeap[0] > arr[i]:
            continue
        # Otherwise Change minimum element
        # (top element of the minHeap) to
        # current element by polling out
        # the top element of the minHeap
        else:
            # deleting top element of the min heap
            minHeap[0] = minHeap[-1]
            minHeap.pop()
            minHeap.append(arr[i])
            # maintaining heap again using
            # O(n) time operation....
            hq.heapify(minHeap)
    # Now min heap contains k maximum
    # elements, Iterate and print
    for i in minHeap:
        print(i, end=" ")


# Driver code
arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
size = len(arr)
# Size of Min Heap
k = 3
FirstKelements(arr, size, k)
'''Code is written by Rajat Kumar.....'''
