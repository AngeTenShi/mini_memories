# ANGE ET PAUL
from turtle import *

def update_progressbar(tentative_pourcentage,t):
    t.clear()
    t.up()
    t.goto(271,703)
    t.down()
    t.setheading(0)
    t.color("green")
    t.begin_fill()
    t.forward(268 - (tentative_pourcentage * 268 // 100))
    t.right(90)
    t.forward(48)
    t.right(90)
    t.forward(268 - (tentative_pourcentage * 268 // 100)) 
    t.right(90)
    t.forward(48)
    t.end_fill()
    update()

def stockx(x,y,c,t):
    print("pass")
    t.up()
    t.goto(x,y)
    t.down()
    t.setheading(0)
    t.fillcolor("green")
    t.begin_fill()
    t.right(59)
    t.forward(c*50)
    t.left(37)
    t.forward(c*18)
    t.left(144)
    t.forward(c*51)
    t.left(28)
    t.goto(x,y)
    t.end_fill()
    t.right(150)#revenir etait initaile angle 0
    t.up()
    t.right(62.5)
    t.forward(c*30.2)
    t.down()
    t.fillcolor("green")
    t.begin_fill()
    t.forward(c*10.3)
    t.right(63)
    t.forward(c*8.5)
    t.right(38)
    t.forward(c*18)
    t.right(146)
    t.forward(c*27.6)
    t.end_fill()
    t.up()
    t.forward(c*11)
    t.down()
    t.fillcolor("green")
    t.begin_fill()
    t.up()
    t.forward(c*2)
    t.down()
    t.forward(c*10.3)
    t.left(129)
    t.forward(c*4.2)
    t.right(148)
    t.forward(c*20.7)
    t.right(123)
    t.forward(c*11.8)
    t.right(92)
    t.forward(c*4.2)
    t.left(62)
    t.forward(c*17)
    t.right(94)
    t.forward(c*5.85)
    t.right(23)
    t.forward(c*5.35)
    t.end_fill()

def carré(c,turtle):
        turtle.color(c)
        turtle.fillcolor(c)
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(9)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(9)

def sneakers(x,y,ct,turtle,color=color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    tracer(0)
    turtle.up()
    turtle.forward(4*ct)
    turtle.down()
    for i in range(24):
        carré(color,turtle)
    turtle.up()    
    turtle.goto(x,ct)
    turtle.down()
    for i in range(4):
        carré(color,turtle)
    for i in range(24):
        carré("white",turtle)
    turtle.up()
    turtle.goto(x,2*ct)
    turtle.down()
    for i in range(5):
        carré("white",turtle)
    for i in range(23):
        carré("grey",turtle)

    turtle.up()
    turtle.goto(x,3*ct)
    turtle.down()
    for i in range(5):
        carré("grey",turtle)
    for i in range(10):
        carré(color,turtle)
    for i in range(7):
        carré("white",turtle)
    for i in range(6):
        carré(color,turtle)

    turtle.up()
    turtle.goto(x,4*ct)
    turtle.down()
    for i in range(14):
        carré(color,turtle)
    for i in range(8):
        carré("white",turtle)
    for i in range(6):
        carré(color,turtle)

    turtle.up()
    turtle.goto(x,5*ct)
    turtle.down()
    for i in range(8):
        carré(color,turtle)
    for i in  range(1):
        carré("white",turtle)
    for i in range(4):
        carré(color,turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(4):
        carré("white",turtle)
    for i in range(5):
        carré(color,turtle)
    turtle.up()
    turtle.goto(x,6*ct)
    turtle.forward(2*ct)
    turtle.down()
    for i in range(7):
        carré("white",turtle)
    for i in range(4):
        carré(color,turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(6):
        carré("black",turtle)
    for i in range(1):
        carré("white",turtle)
    for i in range(5):
        carré(color,turtle)

    turtle.up()
    turtle.goto(x,7*ct)
    turtle.forward(8*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré(color,turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(2):
        carré("black",turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(4):
        carré(color,turtle)

    turtle.up()
    turtle.goto(x,8*ct)
    turtle.forward(10*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré(color,turtle)
    for i in range(2):
        carré("white",turtle)
    for i in range(1):
        carré("black",turtle)
    for i in range(5):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(1):
        carré(color,turtle)
    for i in range(1):
        carré("white",turtle)

    turtle.up()
    turtle.goto(x,9*ct)
    turtle.forward(12*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré(color,turtle)
    for i in range(8):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)

    turtle.up()
    turtle.goto(x,10*ct)
    turtle.forward(14*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(5):
        carré(color,turtle)
    for i in range(2):
        carré("white",turtle)
    for i in range(1):
        carré("black",turtle)
    for i in range(2):
        carré(color,turtle)
    for i in range(3):
        carré("white",turtle)

    turtle.up()
    turtle.goto(x,11*ct)
    turtle.forward(15*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré(color,turtle)
    for i in range(2):
        carré("black",turtle)
    for i in range(5):
        carré(color,turtle)

    turtle.up()
    turtle.goto(x,12*ct)
    turtle.forward(16*ct)
    turtle.down()
    for i in range(2):
        carré("white",turtle)
    for i in range(4):
        carré(color,turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(2):
        carré(color,turtle)

    turtle.up()
    turtle.goto(x,13*ct)
    turtle.forward(17*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(3):
        carré(color,turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(3):
        carré(color,turtle)

    turtle.up()
    turtle.goto(x,14*ct)
    turtle.forward(17*ct)
    turtle.down()
    for i in range(4):
        carré(color,turtle)
    for i in range(1):
        carré("black",turtle)
    for i in range(3):
        carré(color,turtle)
    for i in range(2):
        carré("black",turtle)

    turtle.up()
    turtle.goto(x,15*ct)
    turtle.forward(17*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(5):
        carré(color,turtle)
    for i in range(4):
        carré("black",turtle)

    turtle.up()
    turtle.goto(x,16*9)
    turtle.forward(17*9)
    turtle.down()
    for i in range(3):
        carré(color,turtle)
    for i in range(4):
        carré("black",turtle)

    turtle.up()
    turtle.goto(x,0)
    turtle.forward(4*ct)
    turtle.down()
    turtle.color("black")
    turtle.forward(24*ct)
    turtle.left(90)
    turtle.forward(11*ct)
    turtle.left(90)
    turtle.forward(1*ct)
    turtle.right(90)
    turtle.forward(5*ct)
    turtle.left(90)
    turtle.forward(3*ct)
    turtle.right(90)
    turtle.forward(1*ct)
    turtle.left(90)
    turtle.forward(7*ct)
    turtle.left(90)
    turtle.forward(4*ct)
    turtle.right(90)
    for i in range(3):
        turtle.forward(1*ct)
        turtle.left(90)
        turtle.forward(1*ct)
        turtle.right(90)
    turtle.forward(2*ct)
    turtle.left(90)
    turtle.forward(1*ct)
    turtle.right(90)
    turtle.forward(2*ct)
    turtle.left(90)
    turtle.forward(1*ct)
    turtle.right(90)
    turtle.forward(2*ct)
    turtle.left(90)
    turtle.forward(1*ct)
    turtle.right(90)
    turtle.forward(6*ct)
    turtle.left(90)
    turtle.forward(ct)
    turtle.right(90)
    turtle.forward(2*ct)
    turtle.left(90)
    turtle.forward(5*ct)
    turtle.left(90)
    turtle.forward(4*ct)
    update()

def decor():
    t = Turtle(visible=False)
    tracer(0)
    #---------------------------BARRE DE MENU--------------------------------------#
    x_base = 8
    y_base = 650
    t.up()
    t.goto (x_base,y_base)
    t.color("green")
    t.write("Stock X", font=("Futura", 40, "bold"))
    x_base += 560
    y_base += 13
    t.goto(x_base,y_base)
    t.color("black")
    t.write("Browse", font=("Arial", 20, "normal"))
    x_base += 125
    t.goto(x_base,y_base)
    t.write("News", font=("Arial", 20, "normal"))
    x_base += 100
    t.goto(x_base,y_base)
    t.write("About", font=("Arial", 20, "normal"))
    x_base += 105
    t.goto(x_base,y_base)
    t.write("Help", font=("Arial", 20, "normal"))
    x_base += 87
    t.goto(x_base,y_base)
    t.write("Login", font=("Arial", 20, "normal"))
    x_base += 95
    t.goto(x_base,y_base)
    t.write("Sign up", font=("Arial", 20, "normal"))
    x_base += 120
    t.goto(x_base,y_base)
    t.write("Sell", font=("Arial", 20, "normal"))
    #---------------------------TRAIT INTERMEDIAIRE--------------------------------------#
    t.up()
    t.goto (-80, 640)
    t.color("grey")
    t.down()
    t.goto(1500,640)
    #---------------------------HEADER GAUCHE--------------------------------------------#
    x_base = 44.8
    y_base = 550
    t.up()
    t.goto (x_base,y_base)
    t.color ("black")
    t.write("SNEAKERS", font=("Arial", 23, "bold"))
    y_base -= 50
    t.goto (x_base,y_base)
    t.write("STREETWEAR", font=("Arial", 23, "bold"))
    y_base -= 50
    t.goto (x_base,y_base)
    t.write("ELECTRONICS", font=("Arial", 23, "bold"))
    y_base -= 50
    t.goto (x_base,y_base)
    t.write("TRADING CARDS", font=("Arial", 23, "bold"))
    y_base -= 50
    t.goto (x_base,y_base)
    t.write("COLLECTIBLES", font=("Arial", 23, "bold"))
    y_base -= 50
    t.goto (x_base,y_base)
    t.write("HANDBAGS", font=("Arial", 23, "bold"))
    y_base -= 50
    t.goto (x_base,y_base)
    t.write("WATCHES", font=("Arial", 23, "bold"))
    
    #---------------------------ZONE CENTRALE--------------------------------------------#
    x_base += 410
    y_base = 580
    t.goto(x_base,y_base)
    t.write("Home/ Search/ Marques de Sneakers ", font=("Arial", 14))
    t.goto(x_base, y_base - 40)
    t.write("Parcourir les résultats pour \"Marques de sneakers\" ", font=("Arial", 18))
    
    #-----------------------BARRE DE PROGRESSION------------------------------------------#
    t.goto(270,704)
    t.color("black")
    t.setheading(0)
    t.down()
    t.width(2)
    t.forward(270)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(270)
    t.right(90)
    t.forward(50)
    update()
    #------------------------PETIT LOGO STOCKX--------------------------------------------#
    x_base = 547
    for i in range(15):
        stockx(x_base,715,0.4,t)
        x_base += 50
        update()
    stockx(547,690,0.4,t)
    x_base = 547    
    for i in range(15):
        stockx(x_base,665,0.4,t)
        x_base += 50
        update()
    stockx(x_base-48,690,0.4,t)
    #------------------------SNEAKERS-----------------------------------------------------#
    sneakers(0, 0, 9, Turtle(visible=False),"red")
    sneakers(400, 0, 9, Turtle(visible=False),"purple")
    sneakers(800, 0, 9, Turtle(visible=False),"green")
    update()
