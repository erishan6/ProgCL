# -*- coding: utf-8 -*-
import math
import random

import corpus


class LanguageModel:
    """
        Constructor for LanguageModel class
        :param n is of type int eg. gram size of language model
    """
    def __init__(self, n):
        self.n = n
        self.vocabulary = set()  # vocabulary of the language model
        self.ngrams = []  # current list of ngram sequences ()
        self.counts = {}  # list of ngram words counts
        self.pdf = {}  # list of probability distribution for ngram words

    """
        Gives string representation for the class's object

    """
    def __str__(self):
        return "The value of n in ngram language model is " + str(self.n)

    """
        Loads corpus from file. Trains the language model for the particular file
        :param filename  
    """
    def load(self, filename):
        print(" Loading corpus")
        file = open(filename, "r")
        sentences = file.readlines()
        self.train_file(sentences)

    """
        Internal fucntion for training by files. Has a logic if the file is too large. 
        :param list of sentences eg.   
        sentences = ["No farther, sir; a man may rot even here.", "What, in ill thoughts again?", "And that's true too."]
    """
    def train_file(self, sentences):
        i = 1
        size = len(sentences)
        tmp = ""
        for line in sentences:
            # print(line)
            if i % 20 == 0 or i == size:
                self.train(corpus.tokenize(tmp.lower()))
                tmp = ""
            if i % 1000 == 0 or i == size:
                print(round((i / size) * 100), "% done")
            tmp += line + " "
            i += 1

    """
        Create ngrams for the particular list of tokens and n gram 
        :param tokens is of type list containing tokenize version derived from corpus.tokenize() 
        :param ngramsize is of type int. The value of ngram 
        input  => tokens = ['oh', 'you', 'darling'], ngramsize = 2 
        output => returns ngram sequences eg. [(None, 'oh'), ('oh', 'you'), ('you', 'darling'), ('darling', None)]
    """

    # TODO write unit tests for empty, short token or negative, 0, positive, more than token length
    def get_ngrams(self, tokens, ngramsize):
        newlst = []
        for i in range(ngramsize - 1):
            newlst.append(None)
        newlst += tokens
        for i in range(ngramsize - 1):
            newlst.append(None)
        sequences = [tuple(newlst[i:i + ngramsize]) for i in range(len(newlst) - (ngramsize - 1))]
        # print((sequences))
        return sequences

    """
        Trains your language model with particular list of tokens and learns the n-gram statistics 
        :param lst is of type list containing tokenize version derived from corpus.tokenize()  
        input  => tokens = ['oh', 'you', 'darling']
        
        calculates vocab(set), ngrams(list), counts(dict of dict), pdf(dict of dict)
        vocab  = {None, 'most', 'sir', 'bounteous'}
        ngrams = [(None, 'most'), ('most', 'bounteous'), ('bounteous', 'sir'), ('sir', None)]
        counts = {(None,): {'most': 1}, ('most',): {'bounteous': 1}, ('bounteous',): {'sir': 1}, ('sir',): {None: 1}}
        pdf    = {(None,): {'most': 1.0}, ('most',): {'bounteous': 1.0}, ('bounteous',): {'sir': 1.0}, ('sir',): {None: 1.0}}
    """
    def train(self, lst):
        # print(lst)
        ## TODO add logic for list of list case using instance
        if self.n == 1:
            for word in lst:
                self.vocabulary.add(word)
                if word not in self.counts:
                    self.counts[word] = 1
                self.counts[word] += 1
            # print(self.counts)
            self.pdf = corpus.normalize(self.counts)
            # print(self.pdf)

        else:
            self.ngrams = self.get_ngrams(lst, self.n)
            for word in lst:
                self.vocabulary.add(word)
            self.vocabulary.add(None)
            # print(self.vocabulary)
            # print(self.ngrams)
            for current_ngram_seq in self.ngrams:
                if current_ngram_seq[:(self.n - 1)] not in self.counts.keys():
                    self.counts[current_ngram_seq[:(self.n - 1)]] = {current_ngram_seq[(self.n - 1)]: 1}
                else:
                    localdict = self.counts[current_ngram_seq[:(self.n - 1)]]
                    if current_ngram_seq[(self.n - 1)] not in localdict.keys():
                        localdict[current_ngram_seq[(self.n - 1)]] = 1
                    else:
                        localdict[current_ngram_seq[(self.n - 1)]] += 1
            # print(self.counts)
            self.pdf = self.counts.copy()
            # print(self.pdf)
            for z in self.pdf.keys():
                self.pdf[z] = corpus.normalize(self.pdf[z])
        # print(self.pdf)

    """
            Returns the estimated probability distribution for the next word that occurs after the given token sequence 
            :param tokens is of type list containing tokenize version derived from corpus.tokenize()  
            input  => tokens = ['cat', 'and']
            output => returns dict with probability of next word's prediction eg. lm.p_next(['cat', 'and']) = {'mouse': 0.6, 'dog': 0.4} .
    """
    # TODO fix for unseen seq which is not present in dict
    def p_next(self, tokens):
        if self.n == 1:
            new_text = random.choice(list(self.counts.keys()))
            if new_text == None:
                return self.p_next(tokens)
            return new_text
        else:
            lst = tuple(tokens[-(self.n - 1):])
            return self.pdf[lst]


    """
            Generates a random token sequence according to the underlying probability distribution
    """
    def generate(self):
        res = []
        if self.n == 1:
            length = random.randint(1, 100)
            # print(length)
            for i in range(length):
                res.append(self.p_next(['know']))
        else:

            first_word = (random.choice(list(self.counts.keys())))
            # print(first_word)
            loopbreak = False
            all_none = 0
            for x in first_word:
                if x == None:
                    loopbreak = True
                    all_none += 1
                    # case of all none

                else:
                    res.append(x)
            if all_none == len(first_word):
                self.generate()
            while True:
                if loopbreak:
                    break
                s = corpus.sample(self.p_next(res))
                if s == None:
                    break
                res.append(s)
        return res

    """
            Returns nthroot  
            :param x is of value to be evaluated 
            :param n is of nth root calculation 
    """
    def nthroot(self, x, n):
        return x ** (1 / float(n))

    """
            Calculate the perplexity of the given Language Model. 
            link : https://en.wikipedia.org/wiki/Perplexity
    """
    def perplexity(self):
        # print(math.log(1.5,2))
        res = 0
        if self.n == 1:
            for value in self.pdf.values():
                res += (math.log(value, 2) * -1)

        else:
            for key in self.pdf.keys():
                tmp = self.pdf[key]
                for value in tmp.values():
                    res += (math.log(value, 2) * -1)  # negative log signifies 1/(p(w_i)|p(w_i-1))
        return self.nthroot(res, self.n)


if __name__ == '__main__':
    lm = LanguageModel(2)
    # lm.train([' the ', ' cat ', ' runs ', ' the ', ' cat ', ' the ', ' cat ', ' thea ', ' cat ', ' cat ' ,' the ', ' cats '])
    lm.train(['the', 'dog', 'runs', 'cat'])
    # lst1=[' the ', ' cat ', ' runs ', ' the ', ' cat ', ' the ', ' cat ', ' thea ', ' cat ', ' cat ' ,' the ', ' cats ']
    # lst2 = [' the ', ' dog ', ' runs ' ]
    # lm.train(lst1+lst2)
    # print((lm.counts[(' the ', ' cat ')][' runs ']))
    # print(lm.generate())
    # print(lm.perplexity())
    # print(lm.p_next(['know']))
