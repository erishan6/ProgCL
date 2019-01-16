from constituents import *

sent = Phrase('S', [Phrase('NP', [Token('DT', 'The'), Token('NN', 'cat')]),
                    Phrase('VP', [Token('VB', 'chases'), Phrase('NP', [Token('DT', 'the'), Token('NN', 'mouse')])]),
                    Token('PUNCT', '.')])
# sent = Phrase('S',[""])
print(sent)
