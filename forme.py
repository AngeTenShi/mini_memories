# ANGE ET PAUL
from turtle import *

def carre(x,y,t,color="black"):
        t.up()
        t.goto(x,y)
        t.down()
        t.color(color)
        t.begin_fill()
        for i in range(4):
                t.forward(0.30)
                t.left(90)
                update()
        t.end_fill()

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
