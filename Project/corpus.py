# -*- coding: utf-8 -*-
import string
import random

def tokenize(txt):
    return [word.strip(string.punctuation) for word in txt.split()]

def detokenize(lst):
    res = ""
    for x in lst:
        res+=x+" "
    return res[:-1]

def normalize(tokens):
    res = tokens.copy()
    size=sum(res.values())
    # print()
    # print(size)
    # print(tokens)
    for y in tokens:
        res[y] = res[y]/size
    # print(res)
    return res

def sample(tokens):
    return random.choice(list(tokens.keys()))


if __name__ == '__main__':
    text = "'Oh, you can't help that,' said the Cat: 'we're all mad here. I'm mad. You're mad.'"
    lst = tokenize(text)
    print(lst)
    res = detokenize(lst)
    print(res)
    # normalize(tokenize(text))
    sample({"jj":1,"kk":1, "ll":3})
