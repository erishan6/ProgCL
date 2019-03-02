# -*- coding: utf-8 -*-
import random
import string

"""
    Using string's class for better tokenization.
    :param txt is for string input
"""
def tokenize(txt):
    return [word.strip(string.punctuation) for word in txt.lower().split()]


"""
    Simple detokenization using string concatenation
    :param lst is for giving token seq in list form
"""
def detokenize(lst):
    res = ""
    for x in lst:
        res+=x+" "
    return res.strip()


"""
    Normalizes the dict wrt len of values. Generating new dict in process
    :param tokens is of type dict. eg 
    input  => {'fear': 1, 'sad': 2}
    output => {'fear': 0.3333333333333333, 'sad': 0.6666666666666666}

"""
def normalize(tokens):
    res = tokens.copy()
    size=sum(res.values())
    # print(res)
    for y in tokens:
        res[y] = res[y]/size
    # print(res)
    return res


"""
    Chooses random key word for next prediction. Usage in generate function
    :param tokens is of type dict. eg 
    input  => {'fear': 1, 'sad': 2}
    output => returns key eg. 'fear'or 'sad' for this dictionary

"""
def sample(tokens):
    return random.choice(list(tokens.keys()))


if __name__ == '__main__':
    text = "'Oh, you can't help that,' said the Cat: 'we're all mad here. I'm mad. You're mad.'"
    lst = tokenize(text)
    print(lst)
    res = detokenize(lst)
    print(res)
    sample({"jj":1,"kk":1, "ll":3})
