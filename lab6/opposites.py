# -*- coding: utf-8 -*-

def update(elem):
    return elem[::-1]


def find_opposites(lst):
    mylst = []
    mydict = {}
    for w in lst:
        if w not in mydict.keys():
            mydict[w] = w[::-1]
        if w not in mydict.values():
            continue
        elif w != w[::-1]:
            q = (w[::-1], w)
            mylst.append(q)
    return mylst


# def check(elem,lst):
#     return in_biseact
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


if __name__ == '__main__':
    lst = ["deer", "reed"]
    # lst=[]
    # lst=["abba"]
    lst = ["according", "deer", "net", "ten", "reed", "refer", "raw", "war", "addition", "frequency", "platform"]
    # print(find_opposites(lst))
    print(find_opposites_quickly(lst))
