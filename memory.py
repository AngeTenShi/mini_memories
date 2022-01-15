#ANGE ET PAUL
from turtle import *
import time
import random
from decor import * 
from forme import * 
from logo import *


#Initialisation des variables globales
p_choix = 0
p_choix2 = 0
clicked = 1
niveau = 0
tentative = 0
objects = []
t_case = Turtle(visible=True)
t_progressbar = Turtle(visible=False)
tentative_total = 0

tracer(0)

def choose_objects():
    global niveau
    nbpaire = 0
    if niveau == 1:
        global_coords = [[500,500],[750,500],[1000,500],[500,300],[750,300],[1000,300]] #6 coordonnées
        nbpaire = 3
    if niveau == 2:
        global_coords = [[455,500],[655,500],[855,500],[1055,500],[455,300],[655,300],[855,300],[1055,300]] # 8 coordonées
        nbpaire = 4
    if niveau == 3:
        global_coords = [[455,520],[455,400],[455,280],[655,520],[655,400],[655,280],[855,520],[855,400],[855,280],[1055,520],[1055,400],[1055,280]] # 12 coordonnées
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

def drawLogos(x,y,l,type_objets,t,color):
    if type_objets == "umbro":
        umbro(x-15,y-47,10,t,color)
    if type_objets == "gucci":
        gucci(x,y-5,10,t,color)
    if type_objets == "balenciaga":
        balenciaga(x+100,y-45,10,t,color)
    if type_objets == "lv":
        lv(x+40,y-10,10,t,color)
    if type_objets == "converse":
        converse(x+10,y+20,10,t,color)
    if type_objets == "offwhite":
        offwhite(x+35,y-103,10,t,color)

def make_figure(objects):
    global t_case
    nombre_case = len(objects)
    for i in range(nombre_case):
        if objects[i][3] == 1:
            dessineCase(objects[i][0], objects[i][1],50,t_case,"green")
            update()

        else:
            drawLogos(objects[i][0], objects[i][1],50,objects[i][2],t_case,objects[i][4])
            update()
        update()

def dessineCase(x,y,l,t,c):
    tracer(0)
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.setheading(0)
    t.pensize(10)
    t.begin_fill()
    for i in range(2):
        t.forward(l*3)
        t.right(90)
        t.forward(l*2)
        t.right(90)
        update()
    t.end_fill()
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
        if objects[i][3] == 1:
            x_tab.append(objects[i][0])
            y_tab.append(objects[i][1])
    x = min(x_tab, key=lambda val:abs(val - p_choix[0]))
    y = min(y_tab, key=lambda val:abs(val - p_choix[1]))
    for i in range(len(objects)):
        if objects[i][0] == x and objects[i][1] == y:
            p_index = i
    return p_index

def eventClick(x,y):
    global clicked
    global p_choix
    global p_choix2
    global niveau
    global tentative
    global objects
    global t_case
    global objects
    global tentative_total
    if niveau == 0:
        clearscreen()
        p_choix = 0
        niveau = int(textinput("Level Selection :", "Quel niveau (1,2,3) :"))
        decor()
        objects = choose_objects()
        make_figure(objects)
        if niveau == 1:
            tentative = 40
        if niveau == 2:
            tentative = 30
        if niveau == 3:
            tentative = 20
        tentative_total = tentative
        print(objects)
    else :
        if clicked > 0:
            if p_choix == 0:
                p_choix = [round(x,2), round(y,2)]
                print(p_choix)
            else:
                p_choix2 = [round(x,2), round(y,2)]
                print(p_choix2)
        if clicked == 2:
                game()
        clicked += 1
    onscreenclick(eventClick)

def game(): # Fonction pour jouer
    global p_choix
    global p_choix2
    global clicked
    global tentative
    global objects
    global t_case
    global t_progressbar
    global tentative_total
    onscreenclick(None)
    i = len(objects)
    score_p = 0
    choix, choix2 = player_play(objects,p_choix,p_choix2)
    if tentative == 0:
        update_progressbar(tentative * 100 // tentative_total ,t_progressbar)
        onscreenclick(None)
        time.sleep(500)
        bye()
    t_case.clear()
    if objects[choix][2] == objects[choix2][2]:
        objects[choix][3] = 0
        objects[choix2][3] = 0
        make_figure(objects)
        i = i - 2
        score_p += 1
    else:
        objects[choix][3] = 0
        objects[choix2][3] = 0
        make_figure(objects)
        t_case.clear()
        time.sleep(5)
        objects[choix][3] = 1
        objects[choix2][3] = 1
        make_figure(objects)
        tentative -= 1
    update_progressbar(tentative * 100 // tentative_total ,t_progressbar)
    p_choix = 0
    p_choix2 = 0
    clicked = 0
    update()
    onscreenclick(eventClick)

setup(1280,720)
setworldcoordinates(0, 0, 1280, 720)
tracer(0)
up()
goto(640,360)
down()    
write("CLICK ON THE SCREEN TO BEGIN THE GAME ! ", font=('Arial', 40), align='center')
onscreenclick(eventClick)
done()
