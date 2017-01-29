import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.dp.knapsack01 import knapsack01
from algorithms.dp.all_decodings import all_decodings
from algorithms.dp.max_subarray_sum import max_subarray_sum

class TestDynamicProgrammingAlgorithms(unittest.TestCase):

    def test_knapsack01(self):
        weights = [2, 2, 4, 5]
        benefits = [3, 7, 2, 9]
        self.assertEqual((19, [4, 2, 1]), knapsack01(weights, benefits, 10))

    def test_all_decodings(self):
        self.assertEqual(5, all_decodings('1223'))
        self.assertEqual(3, all_decodings('1234'))

    def test_max_subarray_sum(self):
        self.assertEqual(9, max_subarray_sum([2, -9, 5, 1, -4, 6, 0, -7, 8]))
        self.assertEqual(-1, max_subarray_sum([-1, -2, -3, -4, -5, -6, -7, -8]))
