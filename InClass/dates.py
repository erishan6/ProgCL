# -*- coding: utf-8 -*-
import re

iso_date = re.compile('^(([123][0]{3}|[12][0-9]{3}))-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$')
us_date = re.compile('^((1[0-2]|0[1-9])[/](3[01]|0[1-9]|[12][0-9])[/]([123][0]{3}|[12][0-9]{3}))$')

print(iso_date.fullmatch("3000-11-11"))
print(us_date.fullmatch("01/31/1000"))
