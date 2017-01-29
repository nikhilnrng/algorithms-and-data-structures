import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.dp.knapsack01 import knapsack01
from algorithms.dp.all_decodings import all_decodings

class TestDynamicProgrammingAlgorithms(unittest.TestCase):

    def test_knapsack01(self):
        weights = [2, 2, 4, 5]
        benefits = [3, 7, 2, 9]
        self.assertEqual((19, [4, 2, 1]), knapsack01(weights, benefits, 10))

    def test_all_decodings(self):
        self.assertEqual(5, all_decodings('1223'))
        self.assertEqual(3, all_decodings('1234'))
