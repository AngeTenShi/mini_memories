from turtle import * 

tracer(0)

def carre(x,y,t):
	t.up()
	t.goto(x,y)
	t.down()
	for i in range(4):
		t.forward(5)
		t.left(90)

def tri_carre(x,y,t):
	t.up()
	t.goto(x,y)
	t.down()
	x_base = x
	for i in range(3):
		carre(x,y,t)
		x += 7.5
	x = x_base
	y -= 10
	for i in range(3):
		carre(x,y,t)
		x += 7.5
	x = x_base
	y -= 10
	for i in range(3):
		carre(x,y,t)
		x += 7.5
t = Turtle()
tri_carre(100,100,t)
update()
mainloop()
