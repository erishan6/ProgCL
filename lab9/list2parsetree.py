from constituents import *


def list2parsetree(l):
    print()


if __name__ == '__main__':
    print(list2parsetree(
        ['S', ['NP', ['DT ', 'The'], ['NN', 'cat']], ['VP', ['VB ', 'chases'], ['NP', ['DT ', 'the'], ['NN', 'mouse']]],
         ['PUNCT', '.']]))
