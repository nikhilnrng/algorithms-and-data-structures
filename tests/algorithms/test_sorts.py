import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.sort.quick_sort import QuickSort
from algorithms.sort.merge_sort import MergeSort
from algorithms.sort.heap_sort import HeapSort

class TestSorts(unittest.TestCase):

    def test_quick_sort(self):
        a = [13, 5, 3, 6, 34, 23, 13, 14, 15, 14, 9]
        b = [3, 5, 6, 9, 13, 13, 14, 14, 15, 23, 34]
        qs = QuickSort(a)
        qs.sort()
        self.assertEqual(a, b)

    def test_merge_sort(self):
        a = [13, 5, 3, 6, 34, 23, 13, 14, 15, 14, 9]
        b = [3, 5, 6, 9, 13, 13, 14, 14, 15, 23, 34]
        ms = MergeSort(a)
        ms.sort()
        self.assertEqual(a, b)

    def test_heap_sort(self):
        a = [13, 5, 3, 6, 34, 23, 13, 14, 15, 14, 9]
        b = [3, 5, 6, 9, 13, 13, 14, 14, 15, 23, 34]
        hs = HeapSort(a)
        hs.sort()
        self.assertEqual(a, b)
