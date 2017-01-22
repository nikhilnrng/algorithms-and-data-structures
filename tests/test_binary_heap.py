import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from data_structures.heaps.binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def setUp(self):
        self.bh = BinaryHeap()

    def test_insert(self):
        self.bh.insert(9)
        self.bh.insert(6)
        self.bh.insert(5)
        self.bh.insert(3)
        self.bh.insert(2)
        self.assertEqual([2, 3, 6, 9, 5], self.bh.heap)
        self.assertEqual(5, self.bh.size)

    def test_delete(self):
        self.bh.heapify([21, 19, 18, 17, 11, 14, 9])
        self.bh.delete_min()
        self.assertEqual([11, 17, 14, 18, 19, 21], self.bh.heap)
        self.assertEqual(6, self.bh.size)

    def test_heapify(self):
        self.bh.heapify([21, 19, 18, 17, 11, 14, 9])
        self.assertEqual([9, 11, 14, 17, 19, 21, 18], self.bh.heap)
        self.assertEqual(7, self.bh.size)
