# -*- coding: utf-8 -*-

def find_message(txt, words_filename):
    lst = []
    with open(words_filename, 'r') as myfile:
        for l in myfile.readlines():
            lst.append(l.strip())
    temp = txt.strip().split(" ")
    lst.sort(key=lambda s: (-len(s), s))
    mystring = ""
    for x in temp:
        mystring += x[0]
    for w in lst:
        if w in mystring:
            return w


if __name__ == '__main__':
    # print(find_message("to threw daughter inside. and then a so with help such myths, daughter. noble st. and of could spied three","words.txt"))
    # print(find_message(
    #     "It is very cold and she needs old winter clothes from the basement.",
    #     "words.txt"))
    # print(find_message(
    #     "begged of the to st. man birth him that, they he christmas to one many known for legend the of",
    #     "words.txt"))
    filename = "legend_of_three_purses.txt"
    with open(filename, "r") as myfile:
        data = myfile.read().replace('\n', '').lower()
        print(find_message(data, "words.txt"))
