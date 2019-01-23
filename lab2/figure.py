# -*- coding: utf-8 -*-
import turtle

def drawFigure(size=20, rows=8):
    skk = turtle.Turtle()
    for row in range(rows):
        for col in range(row + 1):
            # print(row, col)
            # skk.colormode(1)
            skk.screen.colormode(255)
            skk.pencolor((255, 0, 0))
            # turtle.colormode(255)
            print(skk.screen.colormode())
            # cor = turtle.pencolor((234, 0, 0))
            skk.fillcolor((255, 0, 0))
            skk.begin_fill()
            for i in range(4):
                skk.forward(size)
                skk.right(90)
            skk.end_fill()
            skk.setx(size * (col + 1))
        skk.sety(-size * (row + 1))
        skk.setx(0)
    turtle.done()

if __name__ == '__main__':
    drawFigure()  # pass number of size and rows for various configuration
