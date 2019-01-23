# -*- coding: utf-8 -*-

def find_maxima(lst):
    res = []
    if len(lst) == 0:
        return res
    else:
        for i in range(len(lst)):
            if i == 0:
                res.append(lst[i])
            else:
                if lst[i] > res[len(res) - 1]:
                    res.append(lst[i])
        return res


if __name__ == '__main__':
    print(find_maxima(
        [95, 56, 54, 37, 16, 1, 47, 52, 69, 29, 66, 57, 81, 51, 36, 35, 28, 33, 72, 82, 72, 0, 24, 28, 94, 87, 58, 14,
         28, 29, 4, 33, 72, 40, 7, 77, 35, 19, 94, 48, 69, 59, 33, 0, 18, 26, 53, 60, 23, 21, 84, 37, 8, 68, 93, 97, 23,
         51, 77, 2, 14, 64, 53, 73, 67, 60, 90, 81, 22, 14, 19, 15, 85, 23, 82, 26, 3, 86, 6, 68, 96, 79, 12, 85, 31,
         46, 45, 28, 89, 40]))
