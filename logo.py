# ANGE ET PAUL
from turtle import *
from forme import *

def balenciaga(x,y,l,t,color="black"):
	t.up()
	t.goto(x,y)
	t.down()
	t.pensize(11)
	t.setheading(0)
	t.color(color)
	t.circle(40,180)
	t.left(90)
	t.forward(150)
	t.left(90)
	t.circle(40,180)
	t.up()
	t.goto(x-20, y)
	t.down()
	t.circle(40,180)
	t.right(90)
	t.forward(-150)
	t.right(90)
	t.circle(40,180)

def umbro(x,y,l,t,color="black"):
	t.up()
	t.goto(x,y)
	t.down()
	t.setheading(0)
	t.pensize(11)
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


def lv(x,y,l,t,color="black"):
	t.setheading(0)
	t.pensize(11)
	drawL(x,y,t,color)
	drawV(x-20,y+10,t,color)

def offwhite(x,y,l,t,color="black"):
	t.up()
	t.goto(x,y)
	t.down()
	t.color(color)
	t.pensize(11)
	t.setheading(0)
	for k in range(4):
		t.forward(30)
		t.up()
		t.forward(30)
		t.down()
		t.forward(30)
		t.left(90)
	t.goto(x+90,y+90)
	t.up()
	t.goto(x+90,y)
	t.down()
	t.goto(x,y+90)
	t.up()
	t.pensize(1)
	t.goto(x-3,y+100)
	t.down()
	t.fillcolor(color)
	t.begin_fill()
	for i in range(2):
		t.forward(97)
		t.left(90)
		t.forward(25)
		t.left(90)
	t.end_fill()

def converse(x,y,l,t,color="black"):
	t.up()
	t.goto(x+20,y-55)
	t.down()
	t.pensize(11)
	t.setheading(0)
	t.color(color)
	t.fillcolor(color)
	t.begin_fill()
	for i in range(5):
		t.forward(30)
		t.up()
		t.forward(25)
		t.down()
		t.forward(30)
		t.right(144)
	t.end_fill()
	t.up()
	t.goto(x+43+20,y-78-55)
	t.down()
	t.circle(65)

def gucci(x,y,l,t,color="black"):
	t.up()
	t.goto(x+55,y-90)
	t.down()
	t.color(color)
	t.setheading(0)
	t.pensize(11)
	t.circle(50)
	t.up()
	t.forward(50)
	t.down()
	t.circle(50)
	t.up()
	t.goto(x-2,y+50)
	t.down()

