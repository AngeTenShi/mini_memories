# ANGE ET PAUL
from turtle import *

def decor():
    t = Turtle(visible=False)
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
    t.write("12 ", font=("Arial", 18, "bold"))
    t.setx(x_base + 7)
    t.write(" résultats pour \"Marques de sneakers\"", font=("Arial", 18))
    update()
