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

def panier(x,y,t):
        t.up()
        t.goto(x,y)
        t.down()
        t.fillcolor("green")
        t.begin_fill()
        t.circle(57)
        t.end_fill()
        t.color("white")
        t.up()
        t.goto(1163,88)
        t.down()
        t.left(180)
        n=0
        while n<=25:
                t.forward(70)
                t.right(90)
                t.forward(0.1)
                t.right(90)
                t.forward(70)
                t.left(90)
                t.forward(0.1)
                t.left(90)
                n=n+0.1
        t.color("white")
        t.pensize(5)
        up()
        t.goto(x,y+92)
        down()
        t.circle(15)
        update()



