# -*- coding: utf-8 -*-

def convert_words(word, n):
    flag = 0
    if word[0].isupper():
        flag = 1
    w = word
    w = w.lower()
    if "very" == w or "really" == w or "so" == w or "hella" == w or "totally" == w or "extremely" == w:
        word = (word + " ") * n
    elif flag == 1:
        word = word.capitalize()
    return word.strip()


def intensify(message, n):
    words = message.split()
    s = ""
    for w in words:
        s += convert_words(w, n) + " "

    s = s.replace("!", "!!").replace(".", "!").replace("?", "?!")
    return s.strip().lstrip()


if __name__ == '__main__':
    s = "I am Really excited for the conference. It ' s gonna be So awesome!"
    print(intensify(s, 2))
