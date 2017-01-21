import random

class QuickSort(object):
    """Sort a list using the quicksort algorithm

    Quicksort sorts a list during the partition phase, as opposed to mergesort
    which partitions a list, sorts the partitions, and then merges everything
    back together. From a divide and conquer perspective, quicksort sorts
    while dividing the list. 

    Quicksort Steps: 

    1. Randomly select a pivot from the array.
    2. Reorder the array such that all elements less than pivot end up below
       the pivot and all elements greater than pivot end up above it. At this
       point, the pivot is in its correct position. 
    3. Recursively run steps 1 and 2 on the remaining lower and upper elements.

    Time Complexity: 

    O(nlog(n)), but worst case O(n^2). Since the partition is 
    selected randomly, we must account for the nearly impossible case where 
    the partition is randomly selected and results in subarrays sized 1 and 
    n-1 every single time. 

    T(n) = 2T(n/2) + O(n) -> f(n) = O(n^(log_2(2)-0)) -> T(n) = O(nlog(n))

    Space Complexity:

    On ideal operation in which the median is selected as a partition of
    all sub-arrays, the left subarray and right subarray experience log(n)
    recursive calls, so the space complexity is O(log(n)). 
    """

    def __init__(self, aList):
        self.aList = aList

    def sort(self):
        self.sort_util(0, len(self.aList) - 1)

    def sort_util(self, start, end):
        if start < end:
            # if start and end indices represent a valid list
            pivot = self.partition(start, end)
            self.sort_util(start, pivot - 1)
            self.sort_util(pivot + 1, end)

    def partition(self, start, end):
        pivot = random.randrange(start, end + 1) # randomly select pivot
        self.swap(pivot, end) # place selected pivot at end of list

        for i in range(start, end):
            # for all values in list, not including pivot
            if self.aList[i] <= self.aList[end]:
                # if value is less than/equal to pivot, place below pivot
                self.swap(i, start)
                start += 1

        self.swap(start, end) # swap pivot to correct position
        return start # return position of the pivot

    def swap(self, x, y):
        temp = self.aList[x]
        self.aList[x] = self.aList[y]
        self.aList[y] = temp
