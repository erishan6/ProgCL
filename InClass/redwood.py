# -*- coding: utf-8 -*-
def height(lst):
    if isinstance(lst, list):
        return 1 + max(height(node) for node in lst)
    else:
        return 0


if __name__ == '__main__':
    print(height([[2, 1], 4, [4, 0]]))
