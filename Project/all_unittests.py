import unittest

import corpus
import lm

"""
Integration test for LanguageModel class. Ables to train with new data after training once. 
"""


class Test_lm(unittest.TestCase):

    def test_check(self):
        self.langM = lm.LanguageModel(2)
        self.assertIsInstance(self.langM, lm.LanguageModel, "Belongs to same class")
        self.langM.train(['the', 'dog', 'runs'])
        print(self.langM.counts)
        print(self.langM.pdf)
        print(self.langM.perplexity())
        print(self.langM.generate())
        self.langM.train(['the', 'cat', 'runs', 'the', 'cat', 'the', 'cat', 'thea', 'cat', 'cat', 'the', 'cats'])
        print(self.langM.counts)
        print(self.langM.pdf)
        print(self.langM.perplexity())
        print(self.langM.generate())

    def test_math_funcs(self):
        self.assertEqual(lm.LanguageModel(2).nthroot(4, 2), 2, "Should be 2")
        self.assertEqual(lm.LanguageModel(2).nthroot(8, 3), 2, "Should be 2")
        self.assertEqual(lm.LanguageModel(2).nthroot(32, 5), 2, "Should be 2")


"""
Unit test for all the utilities functions defined in corpus.py
"""


class Test_corpus(unittest.TestCase):

    def test_tokenize(self):
        text = "Oh you can't help that said the Cat"
        lst = corpus.tokenize(text)
        self.assertEqual(len(lst), 8, "Should be same length ie 8")

    def test_detokenize(self):
        lst = ['oh', 'you', "can't", 'help', 'that', 'said', 'the', 'cat']
        ref_text = "oh you can't help that said the cat"
        ref_text2 = text = "oh you can't help that said the cat "
        text = corpus.detokenize(lst)
        self.assertEquals(ref_text, text, "Should be same text")
        self.assertEquals(ref_text2, text, "Should be same text")

    def test_normalize(self):
        train_dict = {"jj": 1, "kk": 2, "ll": 3, "mm": 2}
        test_dict = {'jj': 0.125, 'kk': 0.25, 'll': 0.375, 'mm': 0.25}
        print(corpus.normalize(train_dict))
        self.assertDictEqual(test_dict, {'jj': 0.125, 'kk': 0.25, 'll': 0.375, 'mm': 0.25}, "Same dictionary")

    def test_sample(self):
        text = corpus.sample({"jj": 1, "kk": 1, "ll": 3})
        self.assertIn(text, ["jj", "kk", "ll"], "Should be from this")


if __name__ == '__main__':
    unittest.main()
