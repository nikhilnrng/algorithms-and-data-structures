import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from data_structures.heaps.binary_heap import BinaryHeap

class HeapSort(BinaryHeap):
    """Sort a list using the heapsort algorithm

    Heapsort converts a list into a heap with a min-heap ordering property and then repeatedly
    deletes the minimum value of the heap until no values are left in the heap. The order of
    deletions results in a sorted list. Note, unlike mergesort, heapsort is not a stable sort, 
    meaning that there is no guarantee that elements of the same value will remain in the same order 
    after the heapsort algorithm is run.

    Heapsort Steps: 

    1. Run heapify() on the list. 
    2. Run delete_min() on the heap until no values are left. 

    Time Complexity: 

    O(nlog(n)). The heap is built in O(n) using heapify(). A single delete_min() operation is O(logn)
    so the total complexity for all n delete_min() operations is O(nlog(n)). Thus, the deletions
    dominate the overall time complexity: O(n + nlog(n)) = O(nlog(n)). 

    Space Complexity: 

    O(n). The heap is built as a separate list, which requires O(n) space. Heapsort can technically
    be done in O(1) space by building a max-heap and placing all delete_max() values at the end of
    the list until the heap is empty. This could also be done with a min-heap to return a list in 
    descending order.
    """

    def __init__(self, alist):
        super(HeapSort, self).__init__()
        self.alist = alist

    def sort(self):
        super(HeapSort, self).heapify(self.alist)

        for i in range(len(self.alist)):
            self.alist[i] = super(HeapSort, self).delete_min()
