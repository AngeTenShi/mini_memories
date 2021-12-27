# ANGE ET PAUL
from turtle import *
from utils.forme import *

def balenciaga(x,y,t,color="black"):
	t.up()
	t.goto(x,y)
	t.down()
	t.color(color)
	t.circle(40,180)
	t.left(90)
	t.forward(150)
	t.left(90)
	t.circle(40,180)
	t.up()
	t.goto(x - 30, y)
	t.down()
	t.circle(40,180)
	t.right(90)
	t.forward(-150)
	t.right(90)
	t.circle(40,180)

def umbro(x,y,t,color="black"):
	t.up()
	t.goto(x,y)
	t.down()
	t.setheading(0)
	t.pensize(15)
	t.color(color)
	t.right(22)
	t.forward(100)
	t.left(45)
	t.forward(100)
	t.left(132)
	t.forward(100)
	t.goto(x,y)
	t.pensize(9)
	t.up()
	t.home()
	t.goto(x+60,y)
	t.down()
	t.right(22)
	t.forward(35)
	t.left(45)
	t.forward(35)
	t.left(132)
	t.forward(35)
	t.goto(x+60,y)


def lv(x,y,t,color="black"):
	t.setheading(0)
	drawL(x,y,t,"red")
	drawV(x-20,y+10,t,"red")

def chanel(x,y,t,color="black"):
	t.up()
	t.goto(x,y)
	t.down()
	t.color(color)
	t.setheading(-90)
	for i in range(300):
		t.forward(1.2)
		t.right(1)
	t.up()
	t.goto(x-100,y)
	t.down()
	t.color(color)
	t.setheading(270)
	for i in range(300):
		t.forward(1.2)
		t.left(1)

def converse(x,y,t,color="black"):
	pass

def gucci(x,y,t):
	pass
