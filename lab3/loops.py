# -*- coding: utf-8 -*-

def sum_except(start, end, omit=None):
    res = 0
    for i in range(start,end):
        if i==omit:
            continue
        res += i
    return res

def sum_step(start, end, step=1):
    res = 0
    for i in range(start,end+1,step):
        res+=i
    return res

def is_prime(x):
    isPrime = True
    if x > 1:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                isPrime = False
                break
    else:
        isPrime = False
    return isPrime

def find_biggest_prime(x):
    if x > 1:
        for i in range(x, int(x ** 0.5), -1):
            if is_prime(i):
                return i
    return None

if __name__ == '__main__':
    print(sum_except(0,6,2))
    print(sum_step(0,6))
    print(is_prime(104593))
    print(find_biggest_prime(10))