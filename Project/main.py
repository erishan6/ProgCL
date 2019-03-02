# -*- coding: utf-8 -*-
import sys

import corpus
import lm


def main():
    while True:

        print("Press 1 : Create a new language model with a user-specified n")
        print("Press 2 : Load texts from a file, and train the language model on those texts")
        print("Press 3 : Generate a text from the language model, and print it to the screen")
        print("Press 4 : Generate a user-specified number of texts from the language model, and write them to a file")
        print("Press 5 : Print the predicted  next word's probability distribution")
        print("Press 6 : Perplexity of language model")
        print("Press 7 : Exit")
        print("Enter your choice (integer) ")
        text = input()
        if text=="1":
            print()
            print("Enter the value of n(integer value)")
            n = int(input())
            c = lm.LanguageModel(n)
            print("The value for ngram language model is ", n, "gram model")

        elif text=="2":
            print()
            print("You have pressed 2")
            print("Enter the filename")
            filename  = input()
            # filename = "dev_shakespeare.txt"
            # lst = c.load(filename)
            c.load(filename)
            # print(lst)
            # c.train(lst)
            # print((c.counts))

        elif text == "3":
            print()
            print("You have pressed 3 ")
            print("Generate a random text")
            print(corpus.detokenize(c.generate()))

        elif text == "4":
            print()
            print("You have pressed 4 ")
            print("Enter the number for how many random texts you want")
            number_random = int(input())
            print("Enter the filename you want to save for random text")
            filename = input()
            file = open(filename, "w")
            while True:
                if number_random == 0:
                    break
                file.write(corpus.detokenize(c.generate()) + "\n")
                number_random -= 1
            file.close()
            # print(c.generate())

        elif text=="5":
            print()
            print("You have pressed 5 ")
            print("Enter the text and predict the next word's probability distribution")
            # s = "venture forth, The better part of my affections"
            s = input().lower()
            print(c.p_next(corpus.tokenize(s)))

        elif text=="6":
            print()
            print("You have pressed 6 ")
            print("Perplexity of the current language model is ", c.perplexity())

        elif text == "7":
            print()
            print("You have pressed 7 for exit")
            # for x in c.pdf:
            #     print(x, c.pdf[x])
            #
            # print(len(c.pdf))
            print("Exiting the main program")
            sys.exit(0)

        else :
            print("Incorrect input. Please enter correct input for selecting option")



if __name__ == '__main__':
    main()