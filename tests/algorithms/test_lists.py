import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.list.search_sorted_list import search_sorted_list

class TestListAlgorithms(unittest.TestCase):

    def test_search_sorted_list(self):
        self.assertEqual(-1, search_sorted_list(5, [1, 2, 3, 4]))
        self.assertEqual(5, search_sorted_list(27, [1, 5, 15, 20, 23, 27]))
        self.assertEqual(-1, search_sorted_list(5, [1, 2, 3, 4, 6, 7, 8, 9]))
        self.assertEqual(0, search_sorted_list(1, [1, 2, 3, 4, 6, 7, 8, 9]))
