import os, sys, unittest, random
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from data_structures.trees.binary_search_tree import BinarySearchTree

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
