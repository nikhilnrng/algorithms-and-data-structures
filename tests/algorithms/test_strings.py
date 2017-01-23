import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.string.word_break import word_break

class TestStringAlgorithms(unittest.TestCase):

    def test_word_break(self):
        adict = ['arrays', 'dynamic', 'heaps', 'IDeserve', 'learn', 'learning', 'linked', 'list', 'platform']
        astr = 'IDeservelearningplatform'
        self.assertEqual(True, word_break(adict, astr))

        adict = ['hello', 'good', 'bye', 'go', 'by']
        astr = 'ahellogoodbye'
        self.assertEqual(False, word_break(adict, astr))
