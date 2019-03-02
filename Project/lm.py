# -*- coding: utf-8 -*-
import corpus
import random
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
        data = file.read()
        lst=corpus.tokenize(data.lower())
        # print(len(lst))
        return lst

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
    # TODO check for if tokens len is less than n gram
    def p_next(self, tokens):
        # print(tokens)
        lst = tuple(tokens[len(tokens)-(self.n-1):])
        # print(lst)
        return self.pdf[lst]


    # generates a random token sequence according to the underlying probability distribution
    def generate(self):
        res = []
        first_word = random.choice(self.lst)
        res.append(first_word)
        print(first_word)

        while True:
            s = corpus.sample(self.p_next(res))
            if s==None:
                break
            # print(s)
            res.append(s)
        print(corpus.detokenize(res))
        return res
    # calculate the perplexity of the given text.
    def perplexity(self):
        print()



if __name__ == '__main__':
    lm  = LanguageModel(2)
    lm.train([' the ', ' cat ', ' runs ', ' the ', ' cat ', ' the ', ' cat ', ' thea ', ' cat ', ' cat ' ,' the ', ' cats '])
    lm.train([' the ', ' dog ', ' runs ' ])
    # lst1=[' the ', ' cat ', ' runs ', ' the ', ' cat ', ' the ', ' cat ', ' thea ', ' cat ', ' cat ' ,' the ', ' cats ']
    # lst2 = [' the ', ' dog ', ' runs ' ]
    # lm.train(lst1+lst2)
    # print((lm.counts[(' the ', ' cat ')][' runs ']))
    # lm.generate()
    print(lm.generate())



