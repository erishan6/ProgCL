# -*- coding: utf-8 -*-
import datetime


def update(elem):
    return elem[::-1]


def finds(elem, lst):
    for x in lst:
        if x == elem[::-1]:
            return elem, x
    return None, None


def find_opposites_quickly(lst):
    mylst = []
    myset = set(lst)
    for w in lst:
        if w[::-1] in myset and w != w[::-1]:
            q = (w, w[::-1])
            mylst.append(q)
            myset.remove(w)
            myset.remove(w[::-1])
    return mylst


def read_words(filename):
    result = []
    for line in open(filename, "r"):
        result.append(line.strip())
    return result


def find_longest(pairs):
    max_len = 0
    max_pair = "", ""
    for (w1, w2) in opp:
        if len(w1) > max_len:
            max_len = len(w1)
            max_pair = w1, w2

    return max_pair


if __name__ == "__main__":
    words = read_words("words.txt")
    print("Read", len(words), "words")
    # word = set(words)
    # print(len(word))

    # running the function
    start_time = datetime.datetime.now()
    opp = find_opposites_quickly(words)
    end_time = datetime.datetime.now()
    total_time = (end_time - start_time).total_seconds()
    #
    print("All found:", len(opp), "(correct: 857)")
    print("It took", str(total_time) + "s", "(correct: less than 10s)")
    #
    # # additional test to see if everything is fine
    # longest = find_longest(opp)
    # print("Longest pair is:", longest, "(correct: stressed, desserts)")
