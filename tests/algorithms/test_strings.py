import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from algorithms.string.word_break import word_break
from algorithms.string.reverse_words import reverse_words
from algorithms.string.string_permutations import string_permutation, string_permutation_swap
from algorithms.string.min_edits import min_edits
from algorithms.string.max_as import max_as
from algorithms.string.parentheses_balanced import parentheses_balanced
from algorithms.string.binary_strings import binary_strings

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

    def test_string_permutations(self):
        self.assertEqual(6, len(string_permutation('abc')))
        self.assertEqual(6, len(string_permutation_swap('abc')))
        self.assertEqual(24, len(string_permutation('abcc')))
        self.assertEqual(24, len(string_permutation_swap('abcc')))

    def test_min_edits(self):
        self.assertEqual(5, min_edits('intention', 'execution'))
        self.assertEqual(7, min_edits('hello', 'goodbye'))
        self.assertEqual(3, min_edits('programming', 'programmer'))

    def test_max_as(self):
        self.assertEqual(max_as(1), 1)
        self.assertEqual(max_as(2), 2)
        self.assertEqual(max_as(3), 3)
        self.assertEqual(max_as(4), 4)
        self.assertEqual(max_as(5), 5)
        self.assertEqual(max_as(6), 6)
        self.assertEqual(max_as(7), 9)
        self.assertEqual(max_as(8), 12)
        self.assertEqual(max_as(9), 16)
        self.assertEqual(max_as(10), 20)
        self.assertEqual(max_as(11), 27)
        self.assertEqual(max_as(12), 36)
        self.assertEqual(max_as(13), 48)
        self.assertEqual(max_as(14), 64)
        self.assertEqual(max_as(15), 81)
        self.assertEqual(max_as(16), 108)

    def test_parentheses_balanced(self):
        self.assertEqual('Invalid', parentheses_balanced('('))
        self.assertEqual('Invalid', parentheses_balanced(')(PHN(X)'))
        self.assertEqual('Invalid', parentheses_balanced('()(PHN(X))'))
        self.assertEqual('Valid', parentheses_balanced('(PHN(X))'))
        self.assertEqual('Valid', parentheses_balanced('((BCD)AE)'))

    def test_binary_strings(self):
        self.assertEqual(3, binary_strings(2))
        self.assertEqual(5, binary_strings(3))
