class MergeSort(object):
    """Sort a list using the mergesort algorithm

    Mergesort sorts a list by dividing the list into two sublists until single
    sublists are left. Then, the sublists are merged until a single, sorted list
    remains.

    Mergesort Steps:

    1. Divide the unsorted list into n single-element sublists.
    2. Merge sublists to produce new sorted sublist until a single sublist 
       remains.

    Time Complexity: 

    O(nlog(n)), as derived from Master Theorem: 

    T(n) = 2T(n/2) + O(n) -> f(n) = O(n^(log_2(2) - 0) -> T(n) = O(nlog(n))

    Space Complexity:

    O(n + logn) -> O(n). O(n) space is required for array merging and O(logn)
    space is required on the stack for recursive calls. In this case, O(n)
    dominates, resulting in overall space complexity of O(n). 
    """

    def __init__(self, lst):
        self.lst = lst

    def sort(self):
        self.sort_util(0, len(self.lst) - 1)

    def sort_util(self, start, end):
        # base case, list sized 0 or 1
        if start >= end:
            return

        # divide into two subarrays
        mid = (start + end) / 2
        self.sort_util(start, mid)
        self.sort_util(mid + 1, end)

        # conquer by merging in sorted order
        self.merge(start, mid, end)

    def merge(self, start, mid, end):
        curr, left, right = (0, start, mid + 1)
        result = [None] * (end - start + 1)

        while left <= mid and right <= end:
            if self.lst[left] <= self.lst[right]:
                # store left if value at left is less than/equal to value at right
                result[curr] = self.lst[left]
                left += 1
            else:
                # store right if value at right is less than value at left
                result[curr] = self.lst[right]
                right += 1
            curr += 1

        # store remaining values from either left or right, if they exist
        if left <= mid:
            result[curr:] = self.lst[left:mid + 1]
        elif right <= end:
            result[curr:] = self.lst[right:end + 1]

        # update the actual list
        self.lst[start:end + 1] = result
