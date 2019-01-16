class Token:
    def __init__(self, pos, word):
        '''
        Construct a token
        Args:
            pos: The part of speech, as a string.  i.e. NN, JJ, etc.
            word: The token's text, as a string
        '''
        self.pos = pos
        self.word = word

    def __str__(self):
        return "(" + self.pos + " " + self.word + ")"


class Phrase:
    def __init__(self, phrase_type, children):
        '''
        Construct a phrase
        Args:
            phrase_type: The phrases type, as a string.  i.e. NP, VP, ADJP, etc.
            children: The phrase's children --- a list.  Each child is
                either a token (a leaf node) or another Phrase (an interior node)
        '''
        self.phrase_type = phrase_type
        self.children = children

    def __str__(self):
        def my_str(lst):
            if len(lst) == 1:
                return str(lst[0])
            else:
                return str(lst[0]) + my_str(lst[1:])
            return str(lst[0] + " " + my_str(lst[1:0]))

        return "(" + self.phrase_type + " " + my_str(self.children) + ")"


if __name__ == '__main__':
    t_the = Token('DT ', 'The ')
    t_cat = Token('NN ', 'cat ')
    p_the_cat = Phrase('NP ', [t_the, t_cat])
    print(str(t_the))
    print(str(t_cat))
    print(str(p_the_cat))
