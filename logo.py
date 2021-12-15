from turtle import *
import time

tracer(0)

def balenciaga(x,y,t):
	t.up()
	t.goto(x,y)
	t.down()
	t.pensize(10)
	t.color("black")
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

def umbro(x,y,t):
	pass

def lv(x,y,t):
	pass

def offwhite(x,y,t):
	pass

def converse(x,y,t):
	pass

def gucci(x,y,t):
	pass


t = Turtle()
balenciaga(0,0,t)
update()
mainloop()
