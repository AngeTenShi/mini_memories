# ANGE ET PAUL
from turtle import *

def carre(x,y,t):
        t.up()
        t.goto(x,y)
        t.down()
        t.color("black")
        t.begin_fill()
        for i in range(4):
                t.forward(0.30)
                t.left(90)
                update()
        t.end_fill()

def tri_carre(x,y,t=Turtle()):
        t.hideturtle()
        t.up()
        t.goto(x,y)
        t.down()
        t.setheading(0)
        t.color("black")
        t.width(1)
        x_base = x
        for i in range(3):
                carre(x,y,t)
                x += 0.42
        x = x_base
        y -= 0.7
        for i in range(3):
                carre(x,y,t)
                x += 0.42
        x = x_base
        y -= 0.7
        for i in range(3):
                carre(x,y,t)
                x += 0.42
        update()

def drawL(x,y,t,color):
        t.up()
        t.goto(x,y)
        t.down()
        t.color(color)
        t.right(90)
        t.forward(80)
        t.left(90)
        t.forward(45)

def drawV(x,y,t,color):
        t.up()
        t.goto(x,y)
        t.down()
        t.color(color)
        t.right(65)
        t.forward(85)
        t.left(135)
        t.forward(85)