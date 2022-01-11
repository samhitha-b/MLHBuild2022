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


def semicircleslayer(tur, orad, irad):
    shift(tur, orad, -10)
    angle = 0
    for i in range(40):
        tur.setheading(angle)
        tur.circle(irad, 180)
        angle = angle + 10


def draw_petal(turt, radius):
    heading = turt.heading()
    turt.circle(radius, 60)
    turt.left(120)
    turt.circle(radius, 60)
    turt.setheading(heading)


def centre(tur, f_radius, f_petals):
    for i in range(f_petals):
        draw_petal(tur, f_radius)
        tur.left(360 / f_petals)


def spiro(tur, R, r, p):
    tur.penup()
    i = 0
    while i < 10 * pi:
        i = i + 0.01
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


def dots(tur, angle, gap, ix, iy, s):
    shift(tur, ix, iy)
    tur.setheading(90)
    for i in range(50):
        tur.penup()
        tur.fd(gap)
        tur.pendown()
        tur.dot(s)
        tur.left(angle)


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
centre(t, 90, 15)

t.pensize(1)
t.pencolor(250,128,114)
drawCircle(t, 100)

t.pensize(1)
t.pencolor(255, 0, 110)
drawCircle(t, 105)


t.pencolor(131, 56, 236)
semicircleslayer(t, 115, 10)

t.pensize(1)
t.pencolor(58, 134, 255)
spiro(t, 170, 8, 20)


t.pencolor(3, 4, 94)
squareLayer(t, -290, -202.5, 580)

t.pensize(1)
t.pencolor(255,160,122)
dots(t, 9, 60, 380, -25, 7)

t.pencolor(255,255,255)
dots(t, 8, 60, 430, -25, 5)

turtle.done()