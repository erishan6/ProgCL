# -*- coding: utf-8 -*-
class ConLLToken:

    def __init__(self, word, lemma, pos, morph):
        self.word = word
        self.lemma = lemma
        self.pos = pos
        self.morph = morph

    def is_capitalized(self):
        return self.word[0].isupper()

    def is_punctuation(self):
        return self.pos == "PUNCT"

    def is_inflected(self):
        res = True
        if self.lemma == self.word:
            res = False
        elif self.word[0].isupper():
            if self.word[0].lower() == self.lemma[0] and self.word[1:] == self.lemma[1:]:
                res = False
        return res

    def get_number(self):
        a = self.morph
        b = a.split("|")
        res = None
        for w in b:
            if "Number=" in w:
                k = w.index("=")
                res = w[k + 1:]
        return res

    def __str__(self):
        return self.word + "," + self.lemma + "," + self.pos + "," + self.morph

    def get_pos(self):
        return self.pos


if __name__ == '__main__':
    tok = ConLLToken("come", "come", "VERB", "Mood=Ind|Number=Sing|Person=3")
    print("Token=", str(tok))
    print("Capitalized?", tok.is_capitalized())
    print("Punctuation?", tok.is_punctuation())
    print("Inflected?", tok.is_inflected())
    print("Number=", tok.get_number())
