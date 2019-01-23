# -*- coding: utf-8 -*-

def S(n):
    if (n == 0):
        return int("1")
    if (n == 1):
        return int("11")
    starting_string = "11"
    for i in range(2, n + 1):
        starting_string += '$'
        l = len(starting_string)
        count = 1
        temp = ""
        for j in range(1, l):
            if (starting_string[j] != starting_string[j - 1]):
                temp += str(count + 0)
                temp += starting_string[j - 1]
                count = 1
            else:
                count += 1
        starting_string = temp
    return int(starting_string)


if __name__ == '__main__':
    n = 6
    print(S(n))
