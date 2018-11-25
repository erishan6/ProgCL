# -*- coding: utf-8 -*-
def eval_upos(gold_filename, pred_filename):
    data_gold = [line.strip().split() for line in open(gold_filename, 'r')]
    data_pred = [line.strip().split() for line in open(pred_filename, 'r')]
    n = 0
    k = 0
    for i in range(len(data_gold)):
        if data_gold[i] == [] and data_pred[i] == []:
            k = k + 1
            # print(data_gold[i])
        elif data_gold[i][3] == data_pred[i][3]:
            n = n + 1
    return n / (len(data_gold) - k)


if __name__ == '__main__':
    print(round(eval_upos("en_gold.conllu", "en_pred.conllu"), 4))
