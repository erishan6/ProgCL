# -*- coding: utf-8 -*-
import turtle


def drawFigure(size=20, rows=8):
    skk = turtle.Turtle()
    for row in range(rows):
        for col in range(row + 1):
            print(row, col)
            for i in range(4):
                skk.forward(size)
                skk.right(90)
            skk.setx(size * (col + 1))
        skk.sety(-size * (row + 1))
        skk.setx(0)
    turtle.done()

if __name__ == '__main__':
    drawFigure()  # pass number of size and rows for various configuration
