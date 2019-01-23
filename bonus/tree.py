# -*- coding: utf-8 -*-
import turtle
from random import randint


def draw_tree(length, branches=4, min_size=10):
    def draw_tree_recur(level, length, branches, min_size):
        if level >= 0 or length >= min_size:
            skk.forward(length)
            skk.left((branches / 2) * angle)
            for i in range(1, branches):
                skk.left(angle)
                draw_tree_recur(level - 1, length / ratio, branches, min_size)
                skk.right(angle)
                draw_tree_recur(level - 1, length / ratio, branches, min_size)
                skk.left((branches) * angle)

        else:
            return

    skk = turtle.Turtle()
    skk.speed(1)
    skk.penup()
    skk.goto(0, -180)
    skk.left(90)
    skk.pendown()

    angle = randint(20, 40)
    ratio = randint(14, 18) / 10
    level = randint(4, 6)
    draw_tree_recur(level, length, branches, min_size)


if __name__ == '__main__':
    # Main Program Starts Here
    draw_tree(200, 2, 20)
    turtle.done()
