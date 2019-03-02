import unittest


class Test_lm(unittest.TestCase):
    ## write unit tests for empty, short token or negative, 0, positive, more than token length for def get_ngrams(self, tokens, ngramsize):


    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()