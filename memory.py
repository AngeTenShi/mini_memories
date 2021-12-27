#ANGE ET PAUL
from turtle import *
import time
import random
from includes.decor import * 
from includes.logos.utils.forme import * 

tracer(0)

def choose_objects():
    global_coords = [[35,50],[52,50],[68,50],[85,50],[35,26],[52,26],[68,26],[85,26],[35,2],[52,2],[68,2],[85,2]]
    global_objects = ['umbro','gucci','balenciaga','lv','converse','chanel']
    global_colors = ['red','blue','green','grey','purple','black','pink']
    objects = []
    for i in range(6):
        x,y = random.choice(global_coords)
        type_object = random.choice(global_objects)
        color = random.choice(global_colors)
        objects.append([x,y,type_object,1,color])
        global_coords.remove([x,y])
        x,y= random.choice(global_coords)
        objects.append([x,y,type_object,1,color])
        global_coords.remove([x,y])
        global_colors.remove(color)       
    return objects

def make_figure(objects,tc):
    nombre_case = len(objects)
    for i in range(nombre_case):
        if objects[i][3] == 1:
            dessineCase(objects[i][0], objects[i][1],10,i,tc,"red")
        else:
            pass
        update()

def dessineCase(x,y,l,n,t,c="blue"):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.begin_fill()
    for i in range(2):
        t.forward(l+3)
        t.left(90)
        t.forward(l+7)
        t.left(90)
        update()
    t.end_fill()
    t.up()
    t.goto(x+l/2-10,y+l/2-10)
    t.down()
    c=t.color()
    t.color("white")
    t.write(str(n),font=('Arial',14,'normal'))
    t.color(c[0])


def game():
    play = 1
    objects = choose_objects()
    decor()
    tri_carre(96,77)
    t_case = Turtle(visible=False)
    make_figure(objects, t_case)
    i = len(objects)
    while(play == 1):
        while(i > 0):
            choix = int(numinput("choix ?","n ?"))
            choix2 = int(numinput("choix 2 ?", "n ?"))
            t_case.clear()
            if objects[choix][2] == objects[choix2][2]: #A MODIFIER
                objects[choix][3] = 0
                objects[choix2][3] = 0
                make_figure(objects, t_case)
                i = i - 2
            else:
                objects[choix][3] = 0
                objects[choix2][3] = 0
                make_figure(objects,t_case)
                time.sleep(3)
                objects[choix][3] = 1
                objects[choix2][3] = 1
                make_figure(objects, t_case)
            time.sleep(3)
        play = int(input("Tu veux rejouer ?? : "))

setup(0.99,0.99)
setworldcoordinates(0, 0, 100, 100)
game()
update()
mainloop()
