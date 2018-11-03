# -*- coding: utf-8 -*-

if __name__ == '__main__':
    myList = []
    while (True):
        tmp = input("Enter a word: ")
        if tmp == "done":
            break
        myList.append(tmp)

    if len(myList) == 0:
        print("no viable input to the dictionary")
    else:
        myList.sort()
        print(myList[0], "comes first in the dictionary")
        print(myList[len(myList) - 1], "comes last in the dictionary")