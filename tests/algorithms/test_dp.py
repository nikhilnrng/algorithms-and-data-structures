import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.dp.knapsack01 import knapsack01

class TestDynamicProgrammingAlgorithms(unittest.TestCase):

    def test_knapsack01(self):
        weights = [2, 2, 4, 5]
        benefits = [3, 7, 2, 9]
        self.assertEqual((19, [4, 2, 1]), knapsack01(weights, benefits, 10))
