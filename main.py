"""
Généralisation. On vous demande maintenant d'écrire un programme qui fonctionnerait pour n objets.  Pour cela, il vous faut gérer une liste d'objets avec leur position, la description de l'objet, et savoir si l'objet est découvert ou pas. Pour l'instant, il s'agit de polygones, deux polygones forment une paire s'ils ont le même nombre de côtés. Créez une liste initiale contenant 6 objets et modifiez la fin du programme en créant la boucle de jeu:
"""

from turtle import *
import time

def ask_object():
    object_list = []
    nb_objets = int(input("Combien d'objets : "))
    for i in range(nb_objets):
        x_pos = int(input("Position en x : "))
        y_pos = int(input("Position en y : "))
        type_object = input("Type d'objet : ")
        cotes_polygone = int(input("Nombres de cotes de la forme : "))
        discover = int(input("Discovered (0 or 1) : "))
        object_list.append([x_pos, y_pos, type_object, cotes_polygone,discover])
    return object_list

def make_figure(objects,tc):
    nombre_case = len(objects)
    for i in range(nombre_case):
        if objects[i][4] == 1:
            dessineCase(objects[i][0], objects[i][1],100,i,tc,"red")
        else:
            polygone(objects[i][0], objects[i][1],objects[i][3], tc ,100)
def polygone(x, y, nbcotes, t, taille):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("blue")
    angle = 360 // nbcotes
    t.begin_fill()
    for i in range(nbcotes):
        t.forward(taille)
        t.left(angle)
    t.end_fill()

def dessineCase(x,y,l,n,t,c="blue"):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.begin_fill()
    for i in range(0,4):
        t.forward(l)
        t.left(90)
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
    tracer(0)
    objects = ask_object() 
    t_case = Turtle()
    make_figure(objects, t_case)
    i = len(objects)
    while(play == 1):
        while(i > 0):
            choix = int(numinput("choix ?","n ?"))
            choix2 = int(numinput("choix 2 ?", "n ?"))
            t_case.clear()
            if objects[choix][3] == objects[choix2][3]:
                objects[choix][4] = 0
                objects[choix2][4] = 0
                make_figure(objects, t_case)
                i = i - 2
            else:
                objects[choix][4] = 0
                objects[choix2][4] = 0
                make_figure(objects,t_case)
                time.sleep(3)
                objects[choix][4] = 1
                objects[choix2][4] = 1
                make_figure(objects, t_case)
            time.sleep(3) 
        play = int(input("Tu veux rejouer ?? : "))
game()
