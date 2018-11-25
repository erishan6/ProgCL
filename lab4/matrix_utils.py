# -*- coding: utf-8 -*-

def transpose(m):
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return result


if __name__ == '__main__':
    b = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
    print(transpose(b))
