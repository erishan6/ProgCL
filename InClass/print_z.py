# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input("Enter the value of n : "))
    a = n
    c = 0
    for i in range(1, n + 1):
        if i == 1:
            print("*" * n)
        a = a - 1
        c = c + 1
        print(" " * a + "*" + " " * c)
        if i == n:
            print("*" * n)
