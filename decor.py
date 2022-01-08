# ANGE ET PAUL
from turtle import *

def carré(c,turtle):
        turtle.color(c)
        turtle.fillcolor(c)
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(9)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(9)

def sneakers(x,y,ct,turtle):
    tracer(0)
    turtle.up()
    turtle.forward(4*ct)
    turtle.down()
    for i in range(24):
        carré("red",turtle)
    turtle.up()    
    turtle.goto(0,ct)
    turtle.down()
    for i in range(4):
        carré("red",turtle)
    for i in range(24):
        carré("white",turtle)
    turtle.up()
    turtle.goto(0,2*ct)
    turtle.down()
    for i in range(5):
        carré("white",turtle)
    for i in range(23):
        carré("grey",turtle)

    turtle.up()
    turtle.goto(0,3*ct)
    turtle.down()
    for i in range(5):
        carré("grey",turtle)
    for i in range(10):
        carré("red",turtle)
    for i in range(7):
        carré("white",turtle)
    for i in range(6):
        carré("red",turtle)

    turtle.up()
    turtle.goto(0,4*ct)
    turtle.down()
    for i in range(14):
        carré("red",turtle)
    for i in range(8):
        carré("white",turtle)
    for i in range(6):
        carré("red",turtle)

    turtle.up()
    turtle.goto(0,5*ct)
    turtle.down()
    for i in range(8):
        carré("red",turtle)
    for i in  range(1):
        carré("white",turtle)
    for i in range(4):
        carré("red",turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(4):
        carré("white",turtle)
    for i in range(5):
        carré("red",turtle)
    turtle.up()
    turtle.goto(0,6*ct)
    turtle.forward(2*ct)
    turtle.down()
    for i in range(7):
        carré("white",turtle)
    for i in range(4):
        carré("red",turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(6):
        carré("black",turtle)
    for i in range(1):
        carré("white",turtle)
    for i in range(5):
        carré("red",turtle)

    turtle.up()
    turtle.goto(0,7*ct)
    turtle.forward(8*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré("red",turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(2):
        carré("black",turtle)
    for i in range(3):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(4):
        carré("red",turtle)

    turtle.up()
    turtle.goto(0,8*ct)
    turtle.forward(10*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré("red",turtle)
    for i in range(2):
        carré("white",turtle)
    for i in range(1):
        carré("black",turtle)
    for i in range(5):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(1):
        carré("red",turtle)
    for i in range(1):
        carré("white",turtle)

    turtle.up()
    turtle.goto(0,9*ct)
    turtle.forward(12*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré("red",turtle)
    for i in range(8):
        carré("white",turtle)
    for i in range(3):
        carré("black",turtle)

    turtle.up()
    turtle.goto(0,10*ct)
    turtle.forward(14*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(5):
        carré("red",turtle)
    for i in range(2):
        carré("white",turtle)
    for i in range(1):
        carré("black",turtle)
    for i in range(2):
        carré("red",turtle)
    for i in range(3):
        carré("white",turtle)

    turtle.up()
    turtle.goto(0,11*ct)
    turtle.forward(15*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(4):
        carré("red",turtle)
    for i in range(2):
        carré("black",turtle)
    for i in range(5):
        carré("red",turtle)

    turtle.up()
    turtle.goto(0,12*ct)
    turtle.forward(16*ct)
    turtle.down()
    for i in range(2):
        carré("white",turtle)
    for i in range(4):
        carré("red",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(2):
        carré("red",turtle)

    turtle.up()
    turtle.goto(0,13*ct)
    turtle.forward(17*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(3):
        carré("red",turtle)
    for i in range(3):
        carré("black",turtle)
    for i in range(3):
        carré("red",turtle)

    turtle.up()
    turtle.goto(0,14*ct)
    turtle.forward(17*ct)
    turtle.down()
    for i in range(4):
        carré("red",turtle)
    for i in range(1):
        carré("black",turtle)
    for i in range(3):
        carré("red",turtle)
    for i in range(2):
        carré("black",turtle)

    turtle.up()
    turtle.goto(0,15*ct)
    turtle.forward(17*ct)
    turtle.down()
    for i in range(1):
        carré("white",turtle)
    for i in range(5):
        carré("red",turtle)
    for i in range(4):
        carré("black",turtle)

    turtle.up()
    turtle.goto(0,16*9)
    turtle.forward(17*9)
    turtle.down()
    for i in range(3):
        carré("red",turtle)
    for i in range(4):
        carré("black",turtle)

    turtle.up()
    turtle.goto(0,0)
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
    x_base = 1
    y_base = 91
    t.up()
    t.goto (x_base,y_base)
    t.color("green")
    t.write("Stock X", font=("Futura", 40, "bold"))
    x_base += 55
    y_base += 1.5
    t.goto(x_base,y_base)
    t.color("black")
    t.write("Browse", font=("Arial", 20, "normal"))
    x_base += 7.5
    t.goto(x_base,y_base)
    t.write("News", font=("Arial", 20, "normal"))
    x_base += 5.7
    t.goto(x_base,y_base)
    t.write("About", font=("Arial", 20, "normal"))
    x_base += 6.5
    t.goto(x_base,y_base)
    t.write("Help", font=("Arial", 20, "normal"))
    x_base += 5.7
    t.goto(x_base,y_base)
    t.write("Login", font=("Arial", 20, "normal"))
    x_base += 6
    t.goto(x_base,y_base)
    t.write("Sign up", font=("Arial", 20, "normal"))
    x_base += 7.5
    t.goto(x_base,y_base)
    t.write("Sell", font=("Arial", 20, "normal"))
    #---------------------------TRAIT INTERMEDIAIRE--------------------------------------#
    t.goto (-5, 88)
    t.color("grey")
    t.down()
    t.goto(102,88)
    #---------------------------HEADER GAUCHE--------------------------------------------#
    x_base = 3.5
    y_base = 77
    t.up()
    t.goto (x_base,y_base)
    t.color ("black")
    t.write("SNEAKERS", font=("Arial", 23, "bold"))
    y_base -= 5
    t.goto (x_base,y_base)
    t.write("STREETWEAR", font=("Arial", 23, "bold"))
    y_base -= 5
    t.goto (x_base,y_base)
    t.write("ELECTRONICS", font=("Arial", 23, "bold"))
    y_base -= 5
    t.goto (x_base,y_base)
    t.write("TRADING CARDS", font=("Arial", 23, "bold"))
    y_base -= 5
    t.goto (x_base,y_base)
    t.write("COLLECTIBLES", font=("Arial", 23, "bold"))
    y_base -= 5
    t.goto (x_base,y_base)
    t.write("HANDBAGS", font=("Arial", 23, "bold"))
    y_base -= 5
    t.goto (x_base,y_base)
    t.write("WATCHES", font=("Arial", 23, "bold"))
    y_base -= 10
    t.goto (x_base,y_base)
    t.write("BELOW RETAIL", font=("Arial", 23, "bold"))
    #---------------------------ZONE CENTRALE--------------------------------------------#
    x_base += 32
    y_base = 77
    t.goto(x_base,77)
    t.write("Home/ Search/ Marques de Sneakers ", font=("Arial", 14))
    t.goto(x_base, y_base - 5)
    t.write("Parcourir ", font=("Arial", 18))
    t.setx(x_base + 5.5)
    t.write("les ", font=("Arial", 18, "bold"))
    t.setx(x_base + 7)
    t.write(" résultats pour \"Marques de sneakers\"", font=("Arial", 18))
    #------------------------SNEAKERS-----------------------------------------------------#
    #sneakers(0, 0, 9, Turtle(visible=False))
    update()