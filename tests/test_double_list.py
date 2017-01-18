import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from data_structures.lists.double_list import DoubleList

class TestDoubleList(unittest.TestCase):

    def setUp(self):
        self.double = DoubleList()

    def test_insert_head(self):
        self.double.insert_head(4)
        self.double.insert_head(3)
        self.double.insert_head(2)
        self.double.insert_head(1)
        self.assertEqual(self.double.show(), '1->2->3->4')
        self.assertEqual(self.double.size, 4)

    def test_remove_head(self):
        self.double.insert_head(4)
        self.double.insert_head(3)
        self.double.insert_head(2)
        self.double.insert_head(1)
        self.double.remove_head()
        self.assertEqual(self.double.show(), '2->3->4')
        self.double.remove_head()
        self.assertEqual(self.double.show(), '3->4')
        self.double.remove_head()
        self.assertEqual(self.double.show(), '4')
        self.double.remove_head()
        self.assertEqual(self.double.show(), '')
        self.assertEqual(self.double.size, 0)

    def test_insert_tail(self):
        self.double.insert_tail(4)
        self.double.insert_tail(3)
        self.double.insert_tail(2)
        self.double.insert_tail(1)
        self.assertEqual(self.double.show(), '4->3->2->1')

    def test_remove_tail(self):
        self.double.insert_tail(4)
        self.double.insert_tail(3)
        self.double.insert_tail(2)
        self.double.insert_tail(1)
        self.double.remove_tail()
        self.assertEqual(self.double.show(), '4->3->2')
        self.double.remove_tail()
        self.assertEqual(self.double.show(), '4->3')
        self.double.remove_tail()
        self.assertEqual(self.double.show(), '4')
        self.double.remove_tail()
        self.assertEqual(self.double.show(), '')
        self.assertEqual(self.double.size, 0)

    def test_remove_node(self):
        self.double.insert_head(4)
        self.double.insert_head(3)
        self.double.insert_head(2)
        self.double.insert_head(1)
        self.double.remove_node(2)
        self.assertEqual(self.double.show(), '1->3->4')
        self.double.remove_node(3)
        self.assertEqual(self.double.show(), '1->4')
        self.double.remove_node(4)
        self.assertEqual(self.double.show(), '1')
        self.double.remove_node(1)
        self.assertEqual(self.double.show(), '')
        self.assertEqual(self.double.size, 0)

if __name__ == '__main__':
    unittest.main()
