# -*- coding: utf-8 -*-

def average(m):
    size = len(m)
    res = 0
    n = 0
    for r in m:
        for c in r:
            res += c
            n += 1
    return res / n


if __name__ == '__main__':
    b = [[1, 2, 3], [2, 4, 6], [3, 6, 9], [1, 1, 1]]
    print(average(b))
