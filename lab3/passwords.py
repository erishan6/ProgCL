# -*- coding: utf-8 -*-
from fragments import get_random_text

def easy_password(x):

    def easy_password_for_even(k):
        tmp = ""
        while k >0:
            if k==0:
                break
            rad_t = get_random_text()
            if len(rad_t) == 2:
                tmp+=rad_t
                k-=2
        return tmp
    msg = ""
    if x % 2 != 0:
        while True:
            rad_t = get_random_text()
            if len(rad_t) == 3:
                msg+=rad_t
                x -=3
                break
    msg+=easy_password_for_even(x)
    return msg

if __name__ == '__main__':
    print(easy_password(10))



