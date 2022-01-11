import turtle
from math import *


def shift(tur, xcor, ycor):
    tur.penup()
    tur.goto(xcor, ycor)
    tur.pendown()


def drawSquare(tur, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        tur.forward(sz)
        tur.left(90)


def drawCircle(tur, rad):
    shift(tur, 0, -rad)
    tur.setheading(0)
    tur.circle(rad)



def spiro(tur, R, r, p):
    tur.penup()
    i = 0
    while i < 10 * pi:
        i = i + 0.09
        x = (R - r) * cos(i) - (r + p) * cos((R - r) / r * i)
        y = (R - r) * sin(i) - (r + p) * sin((R - r) / r * i)
        tur.goto(x, y)
        tur.pendown()


def squareLayer(tur, ix, iy, sidelength):
    tur.setheading(0)
    shift(tur, ix, iy)
    for i in range(40):
        tur.forward(sidelength)
        tur.left(110)



t = turtle.Turtle()  # create an instance of the turtle and name it t
screen = turtle.Screen()
screen.colormode(255)
t.speed(0)
turtle.bgcolor("#FFFF8B")
turtle.bgcolor("black")
screen.setup(1000, 900)
screen.title("Art Integration Project")
t.hideturtle()
t.pencolor(255, 190, 11)

t.pensize(1)
t.pencolor(250,128,114)
drawCircle(t, 100)

t.pensize(1)
t.pencolor(255, 0, 110)
drawCircle(t, 105)


t.pensize(1)
t.pencolor(58, 134, 255)
spiro(t, 170, 8, 20)


t.pencolor(3, 4, 94)
squareLayer(t, -290, -202.5, 580)

turtle.done()