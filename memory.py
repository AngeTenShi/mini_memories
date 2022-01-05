#ANGE ET PAUL
from turtle import *
import time
import random
from includes.decor import * 
from includes.logos.utils.forme import * 

p_choix = 0
p_choix2 = 0
clicked = 0

def choose_objects(niveau):
    nbobj = 0
    if niveau == 1:
        global_coords = [] #6 coordonnées
        nbpaire = 3
    if niveau == 2:
        global_coords = [] # 8 coordonées
        nbpaire = 4
    if niveau == 3:
        global_coords = [[35,50],[52,50],[68,50],[85,50],[35,26],[52,26],[68,26],[85,26],[35,2],[52,2],[68,2],[85,2]] # 12 coordonnées
        nbpaire = 6
    global_objects = ['umbro','gucci','balenciaga','lv','converse','offwhite']
    global_colors = ['red','blue','green','grey','purple','black','pink']
    objects = []
    for i in range(nbpaire):
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
    tracer(0)
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
    update()

def player_play(objects,p_choix,p_choix2):
    choix = match_coords_with_index(objects, p_choix)
    choix2 = match_coords_with_index(objects, p_choix2)
    return choix, choix2

def match_coords_with_index(objects,p_choix):
    x_tab = []
    y_tab = []
    x = 0
    y = 0
    for i in range(len(objects)):
        x_tab.append(objects[i][0])
        y_tab.append(objects[i][1])
    x = min(x_tab, key=lambda val:abs(val - p_choix[0]))
    y = min(y_tab, key=lambda val:abs(val - p_choix[1]))
    print(f"Valeur de x : {x}") #DEBUG
    print(f"Valeur de y : {y}") #DEBUG
    for i in range(len(objects)):
        if objects[i][0] == x and objects[i][1] == y:
            p_index = i
    return p_index

def eventClick(x,y):
    global clicked
    global p_choix
    global p_choix2
    onclick(None)
    try :
        niveau
    except :
        clearscreen()
        niveau = base()
        clearscreen()
        t_case = Turtle(visible=False)
        objects = choose_objects(niveau)
        make_figure(objects, t_case)
        tri_carre(96,77)
        update()
        if niveau == 1:
            tentative = 3
        if niveau == 2:
            tentative = 2
        if niveau == 3:
            tentative = 1
    if p_choix == 0:
        p_choix = [round(x,2), round(y,2)]
    else:
        p_choix2 = [round(x,2), round(y,2)]
    if clicked == 2:
        if tentative > 0:
            objects = game(objects, niveau)
            tentative -= 1
    clicked += 1

def game(objects,niveau): # Fonction pour jouer
    i = len(objects)
    score_p = 0
    choix, choix2 = player_play(objects,p_choix,p_choix2)
    t_case.clear()
    if objects[choix][2] == objects[choix2][2]:
        objects[choix][3] = 0
        objects[choix2][3] = 0
        make_figure(objects, t_case)
        i = i - 2
        score_p += 1
    else:
        objects[choix][3] = 0
        objects[choix2][3] = 0
        make_figure(objects,t_case)
        time.sleep(3)
        objects[choix][3] = 1
        objects[choix2][3] = 1
        make_figure(objects, t_case)
    p_choix = 0
    p_choix2 = 0
    update()
    return objects

def base():
    bgcolor("black")
    up()
    goto(50,92)
    down()
    color("white")
    write('Level Selection !', font=('Arial', 43), align='center')
    x = 20
    for i in range(3):
        carre(x, 50, Turtle(visible=False), "green")
        x += 20
    update()
tracer(0)
setup(0.99,0.99)
setworldcoordinates(0, 0, 100, 100)
onscreenclick(eventClick)
up()
goto(50,50)
down()
write("CLICK ON THE SCREEN TO BEGIN THE GAME ! ", font=('Arial', 43), align='center')
update()
done()
