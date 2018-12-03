# -*- coding: utf-8 -*-

def sort(lst):  # bubble sort algo
    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


if __name__ == '__main__':
    animals = ["fish", "zebra", "cat", "bat", "dog"]
    print(sort(animals))
