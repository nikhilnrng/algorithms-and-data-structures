import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from data_structures.lists.double_list import DoubleList

class TestLists(unittest.TestCase):

    def test_double_list(self):
        dl = DoubleList()

        dl.insert_head(4)
        dl.insert_head(3)
        dl.insert_head(2)
        dl.insert_head(1)
        self.assertEqual(dl.show(), '1->2->3->4')
        self.assertEqual(dl.size, 4)

        dl.remove_head()
        self.assertEqual(dl.show(), '2->3->4')
        dl.remove_head()
        self.assertEqual(dl.show(), '3->4')
        dl.remove_head()
        self.assertEqual(dl.show(), '4')
        dl.remove_head()
        self.assertEqual(dl.show(), '')
        self.assertEqual(dl.size, 0)

        dl.insert_tail(4)
        dl.insert_tail(3)
        dl.insert_tail(2)
        dl.insert_tail(1)
        self.assertEqual(dl.show(), '4->3->2->1')

        dl.remove_tail()
        self.assertEqual(dl.show(), '4->3->2')
        dl.remove_tail()
        self.assertEqual(dl.show(), '4->3')
        dl.remove_tail()
        self.assertEqual(dl.show(), '4')
        dl.remove_tail()
        self.assertEqual(dl.show(), '')
        self.assertEqual(dl.size, 0)

        dl.insert_head(4)
        dl.insert_head(3)
        dl.insert_head(2)
        dl.insert_head(1)
        dl.remove_node(2)
        self.assertEqual(dl.show(), '1->3->4')
        dl.remove_node(3)
        self.assertEqual(dl.show(), '1->4')
        dl.remove_node(4)
        self.assertEqual(dl.show(), '1')
        dl.remove_node(1)
        self.assertEqual(dl.show(), '')
        self.assertEqual(dl.size, 0)
