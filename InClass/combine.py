# -*- coding: utf-8 -*-


def combine_dict(d1, d2):
    res = {}
    for x in d1:
        res[x] = d1[x]
    for x in d2:
        if x not in res.keys():
            res[x] = d2[x]
        else:
            res[x] += d2[x]
    return res


if __name__ == '__main__':
    d1 = {"a": 10, "b": 1, "c": 15}
    d2 = {"a": 1, "c": 2, "d": 20}
    result = combine_dict(d1, d2)
    print("d1", d1)
    print("d2", d2)
    print("result", result)
