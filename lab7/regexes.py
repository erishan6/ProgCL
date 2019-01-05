# -*- coding: utf-8 -*-
import re

even = re.compile('^\d*[02468]$')
decimal = re.compile('^[0-9](\.[0-9]+)?$')
variable = re.compile('^[a-zA-Z$_][a-zA-Z0-9$_]*$')
quote = re.compile('^\"(.+?)\"')

print(even.fullmatch("3001"))
print(decimal.fullmatch("1.1.1"))
print(variable.fullmatch("we 122"))
print(quote.fullmatch('"hit here'))
