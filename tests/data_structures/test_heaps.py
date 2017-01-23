import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from data_structures.heaps.binary_heap import BinaryHeap

class TestHeaps(unittest.TestCase):

    def test_binary_heap(self):
        bh = BinaryHeap()

        bh.insert(9)
        bh.insert(6)
        bh.insert(5)
        bh.insert(3)
        bh.insert(2)
        self.assertEqual([2, 3, 6, 9, 5], bh.heap)
        self.assertEqual(5, bh.size)

        bh.heapify([21, 19, 18, 17, 11, 14, 9])
        self.assertEqual([9, 11, 14, 17, 19, 21, 18], bh.heap)
        self.assertEqual(7, bh.size)

        bh.delete_min()
        self.assertEqual([11, 17, 14, 18, 19, 21], bh.heap)
        self.assertEqual(6, bh.size)
