# -*- coding: utf-8 -*-
import math


def product(num):
    if not num:
        return 1
    return num[0] * product(num[1:])


def squares(num):
    if len(num) == 1:
        return [num[0] ** 2]
    else:
        return [num[0] ** 2] + squares(num[1:])


def is_prime(n):
    def prime(n, j):
        if n < 2:
            return False
        if j >= int(math.sqrt(n)):
            return True
        if n % j == 0:
            return False
        return prime(n, j + 1)

    return prime(n, 2)


if __name__ == '__main__':
    print(product([8]))
    print(squares([-1]))
    print(is_prime(751))
