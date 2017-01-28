import os, sys, unittest, random
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from data_structures.trees.binary_search_tree import BinarySearchTree
from data_structures.trees.binary_heap import BinaryHeap

class TestTreeDataStructures(unittest.TestCase):

    def test_binary_search_tree(self):
        # initialize test variables
        BST = BinarySearchTree()
        seq = range(1000)

        # randomly insert values into BST
        random.shuffle(seq)
        for val in seq:
            BST.insert(val)
            self.assertEqual(BST.find(val), val)

        # test that values are present in BST
        for val in seq:
            self.assertEqual(BST.find(val), val)

        # test inorder traversal of BST
        seq.sort()
        self.assertEqual(BST.traverse(), seq)

        # randomly remove values from BST
        random.shuffle(seq)
        for val in seq:
            self.assertEqual(BST.find(val), val)
            BST.delete(val)
            self.assertEqual(BST.find(val), None)

        # test that values are not present in BST
        for val in seq:
            self.assertEqual(BST.find(val), None)

    def test_binary_heap(self):
        BH = BinaryHeap()

        BH.insert(9)
        BH.insert(6)
        BH.insert(5)
        BH.insert(3)
        BH.insert(2)
        self.assertEqual([2, 3, 6, 9, 5], BH.heap)
        self.assertEqual(5, BH.size)

        BH.heapify([21, 19, 18, 17, 11, 14, 9])
        self.assertEqual([9, 11, 14, 17, 19, 21, 18], BH.heap)
        self.assertEqual(7, BH.size)

        BH.delete_min()
        self.assertEqual([11, 17, 14, 18, 19, 21], BH.heap)
        self.assertEqual(6, BH.size)
