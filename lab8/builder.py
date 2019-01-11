# -*- coding: utf-8 -*-
import conlltoken


class ConLLUTokenBuilder:

    def buildToken(self, line):
        lst = line.split()
        return conlltoken.ConLLToken(lst[1], lst[2], lst[3], lst[5])


class ConLL09TokenBuilder:

    def buildToken(self, line):
        lst = line.split()
        return conlltoken.ConLLToken(lst[1], lst[2], lst[4], lst[6])


class SplitTokenBuilder:

    def buildToken(self, line):
        lst = line.split("&")
        return conlltoken.ConLLToken(lst[0], lst[1], lst[2], lst[3])


if __name__ == '__main__':
    builder = ConLLUTokenBuilder()
    line = "1   The the DET _ Definite=Def|PronType=Art _ _ _ _"
    tok = builder.buildToken(line)
    print("From ConLLU:", str(tok))

    builder = SplitTokenBuilder()
    line = "courts&court&NOUN&Number=Plur"
    tok = builder.buildToken(line)
    print("From Split:", str(tok))
