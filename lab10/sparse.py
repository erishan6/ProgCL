# -*- coding: utf-8 -*-
class SparseVector:

    def __init__(self, length):
        self.length = length
        self.mydict = {}
        self.mydict.keys()

    def __len__(self):
        return self.length

    def set_pos(self, position, element):
        self.mydict[position] = element

    def get_pos(self, position):
        if position in self.mydict.keys():
            return self.mydict[position]
        return 0

    def __str__(self):
        lst = list(self.mydict.keys())
        # lst.sort()
        s = "SparseVector["
        for i in range(self.length):
            if i in lst:
                s += str(self.mydict[i]) + ","
            else:
                s += "0,"
        s = s[0:len(s) - 1]
        s += "]"
        return s

    def concatenate(self, v):
        res = SparseVector(self.length + len(v))
        res.mydict = self.mydict
        for key in v.mydict.keys():
            res.mydict[self.length + key] = v.mydict[key]
        return res


if __name__ == '__main__':
    v1 = SparseVector(10)
    v2 = SparseVector(5)
    print("Len of v1 =", len(v1))
    print("Len of v2 =", len(v2))

    print("v1 at pos 4 =", v1.get_pos(4))
    v1.set_pos(4, 2)
    print("v1 at pos 4 =", v1.get_pos(4))
    print("v2 at pos 0 =", v2.get_pos(0))
    v2.set_pos(0, 7)
    print("v2 at pos 0 =", v2.get_pos(0))

    print("v1 is ", str(v1))
    print("v2 is ", str(v2))

    v3 = v1.concatenate(v2)
    v4 = v2.concatenate(v1)
    print("v3 is ", str(v3))
    print("v4 is ", str(v4))
