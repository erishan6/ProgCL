# -*- coding: utf-8 -*-

def can_be_composed(word1, word2):
    mydict = {}
    for s in word2:
        if s not in mydict.keys():
            mydict[s] = 1
        else:
            mydict[s] += 1
    for s in word1:
        if s not in mydict.keys():
            return False
        elif mydict[s] == 0:
            return False
        else:
            mydict[s] -= 1

    return True


if __name__ == '__main__':
    print(can_be_composed("python", "ponytail"))
