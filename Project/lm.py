# -*- coding: utf-8 -*-
import math
import random

import corpus


class LanguageModel:

    def __init__(self, n):
        self.n = n
        self.lst = [] # empty data
        self.vocabulary = set()
        self.ngrams=[]
        self.counts = {}
        self.pdf = {}

    def __str__(self):
        return str(self.n)

    # loads the corpus in the lst type
    def load(self, filename):
        print(" Loading corpus")
        file = open(filename, "r")
        # pad = "PAD "*(self.n-1)
        # print(pad)
        # data = pad+file.read()+pad
        data = file.readlines()
        # print(data)
        self.train_file(data)

    # list of sentences in file
    def train_file(self, sentences):
        i = 1
        size = len(sentences)
        tmp = ""
        for line in sentences:
            # print(line)
            if i % 1000 == 0 or i == size:
                print(i)
                self.train(corpus.tokenize(tmp.lower()))
                tmp = ""
            tmp += line + " "
            i += 1

    # write unit tests for empty, short token or negative, 0, positive, more than token length
    def get_ngrams(self, tokens, ngramsize):
        newlst = []
        for i in range(ngramsize - 1):
            newlst.append(None)
        newlst += tokens
        for i in range(ngramsize - 1):
            newlst.append(None)
        # return newlst
        sequences = [tuple(newlst[i:i + ngramsize]) for i in range(len(newlst) - (ngramsize - 1))]
        # print((sequences))
        return sequences

    # trains your language model and learns the n-gram statistics
    def train(self, lst):
        # print(lst)
        self.lst = lst
        ## TODO add logic for list of list case using instance
        self.ngrams=self.get_ngrams(lst,self.n)
        for x in lst:
            self.vocabulary.add(x)
        self.vocabulary.add(None)
        # print(self.vocabulary)
        # print(self.ngrams)
        for x in self.ngrams:
            # print(x[:2], x[2])
            if x[:(self.n-1)] not in self.counts.keys():
                self.counts[x[:(self.n-1)]] = {x[(self.n-1)]:1}
            else:
                localdict = self.counts[x[:(self.n-1)]]
                # print(localdict)
                if x[(self.n-1)] not in localdict.keys():
                    localdict[x[(self.n-1)]]=1
                else:
                    localdict[x[(self.n-1)]]+=1
        # print(self.counts)
        self.pdf = self.counts.copy()
        # print(self.pdf)
        for z in self.pdf.keys():
            self.pdf[z] = corpus.normalize(self.pdf[z])
        # print(self.pdf)

    # returns the estimated probability distribution for the next word that occurs after the given token sequence
    # TODO fix for unseen seq which is not present in dict
    def p_next(self, tokens):
        # print(tokens)
        # print("to search this ", tokens[-(self.n-1):])
        lst = tuple(tokens[-(self.n - 1):])
        return self.pdf[lst]


    # generates a random token sequence according to the underlying probability distribution
    def generate(self):
        res = []
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
            # print(s)
            tmp = self.p_next(res)
            s = corpus.sample(tmp)
            if s == None:
                break
            res.append(s)
        return res

    def nthroot(self, x, n):
        return x ** (1 / float(n))

    # calculate the perplexity of the given text.
    def perplexity(self):
        # print(math.log(1.5,2))
        res = 0
        for x in self.pdf.keys():
            tmp = self.pdf[x]
            for y in tmp.values():
                res += (math.log(y, 2) * -1)  # negative log signifies 1/(p(w_i)|p(w_i-1))
        return self.nthroot(res, self.n)




if __name__ == '__main__':
    lm = LanguageModel(3)
    lm.train([' the ', ' cat ', ' runs ', ' the ', ' cat ', ' the ', ' cat ', ' thea ', ' cat ', ' cat ' ,' the ', ' cats '])
    lm.train([' the ', ' dog ', ' runs ', ' runs '])
    # lst1=[' the ', ' cat ', ' runs ', ' the ', ' cat ', ' the ', ' cat ', ' thea ', ' cat ', ' cat ' ,' the ', ' cats ']
    # lst2 = [' the ', ' dog ', ' runs ' ]
    # lm.train(lst1+lst2)
    # print((lm.counts[(' the ', ' cat ')][' runs ']))
    # lm.generate()
    # print(lm.generate())
    print(lm.perplexity())
