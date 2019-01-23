# -*- coding: utf-8 -*-
import turtle
from ast import literal_eval as make_tuple


def draw_picture(filename, size=10):
    skk = turtle.Turtle()
    skk.pencolor("white")
    skk.speed(0)
    skk.penup()
    skk.goto(-200, -200)
    skk.left(90)
    skk.pendown()
    with open(filename, "rb") as f:
        j = 1
        skk.screen.colormode(255)
        for i in f.readlines():
            temp = i.decode("utf-8").strip().split(" ")
            skk.goto(-200 + j * size, -200)
            skk.pencolor("white")
            skk.forward(-size)
            for t in range(len(temp)):
                if t == 0:
                    skk.pencolor("white")
                skk.forward(size)
                tup = make_tuple(temp[t])
                skk.pencolor(tup)
                skk.fillcolor(tup)
                skk.begin_fill()
                for i in range(4):
                    skk.forward(size)
                    skk.right(90)
                skk.end_fill()
                #

            j += 1


if __name__ == '__main__':
    draw_picture("secret_picture.txt", 4)
    turtle.done()
