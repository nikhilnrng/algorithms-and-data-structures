import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.string.word_break import word_break
from algorithms.string.reverse_words import reverse_words

class TestStringAlgorithms(unittest.TestCase):

    def test_word_break(self):
        adict = ['arrays', 'dynamic', 'heaps', 'IDeserve', 'learn', 'learning', 'linked', 'list', 'platform']
        astr = 'IDeservelearningplatform'
        self.assertEqual(True, word_break(adict, astr))

        adict = ['hello', 'good', 'bye', 'go', 'by']
        astr = 'ahellogoodbye'
        self.assertEqual(False, word_break(adict, astr))

    def test_reverse_words(self):
        reverse = reverse_words(' reverse  a   string    ')
        self.assertEqual('    string   a  reverse ', reverse)

        reverse = reverse_words('  ')
        self.assertEqual('  ', reverse)

        reverse = reverse_words('a')
        self.assertEqual('a', reverse)
