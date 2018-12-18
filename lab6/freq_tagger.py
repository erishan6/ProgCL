# -*- coding: utf-8 -*-
import collections


def train(train_file):
    data_gold = [line.strip().split() for line in open(train_file, 'r')]
    model = {}
    for i in range(len(data_gold)):
        if data_gold[i] == []:
            continue
        else:
            word, tag = data_gold[i][1].lower(), data_gold[i][3]
            # print(word)
            if word not in model.keys():
                ordd = collections.OrderedDict()
                ordd[tag] = 1
                model[word] = ordd
            else:
                tmp = model[word]
                if tag not in tmp.keys():
                    tmp[tag] = 1
                else:
                    tmp[tag] += 1
                model[word] = tmp
    return model


def takeSecond(elem):
    return elem[1]


def train_and_tag(train_file, test_words):
    lst = []
    model = train(train_file)
    # print(model)
    # for x,y in model.items():
    #     print(x,y)
    for w in test_words:
        if w.lower() not in model.keys():
            lst.append("UNK")
        else:
            items = list(model[w.lower()].items())  # .sort(key=takeSecond,reverse=True)
            items.sort(key=takeSecond, reverse=True)
            a, b = items[0]
            # print(items)
            lst.append(a)

    return lst


if __name__ == '__main__':
    # print(train_and_tag("small_train.conllu", [ "This", "is", "my", "wish" ]))
    # train_and_tag("small_train.conllu", ["This", "is", "my", "wish"])
    print(train_and_tag("../lab4/en_gold.conllu", ['Something', 'that', 'is', 'not', 'in', 'the', 'doucment']))
