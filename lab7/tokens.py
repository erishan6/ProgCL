# -*- coding: utf-8 -*-
import re


def tokenize(text):
    res = []
    words = text.split()
    text.isupper()
    for w in words:
        if '\'' in w:
            temp = w.split("\'")
            if temp[1] == 's':
                res.append(temp[0])
                res.append("\'" + temp[1])
            else:
                n = len(temp[0])
                a, b = temp[0][0:n - 1], temp[0][n - 1:n]
                res.append(a)
                res.append(b + "\'" + temp[1])
        else:
            if w in ["Mr.", "Mrs.", "Ms.", "Dr."]:
                res.append(w)
            else:
                temp = re.findall("[A-Za-z@#]+|\S", w)
                for x in temp:
                    res.append(x)

    return res


if __name__ == '__main__':
    print(tokenize(
        'Mr. Brown opened the door and said with a smile, "I can\'t believe it! It\'s such a pleasure to see you!" '))
