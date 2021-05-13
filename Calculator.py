import turtle

sc = turtle.Screen()
sc.bgcolor("black")
turtle.delay(0)

mypen = turtle.Turtle()
mypen.color("cyan")
mypen.penup()
mypen.setposition(-350, -375)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)

mydiapen = turtle.Turtle()
mydiapen.color("white")
mydiapen.penup()
mydiapen.setposition(-350, -375)
mydiapen.pendown()
mydiapen.pensize(3)
mydiapen.speed(0)

myclick = turtle.Turtle()
myclick.color("white")
myclick.penup()
myclick.setposition(-350, -375)
myclick.pensize(3)
myclick.speed(0)
myclick.shapesize(2, 2, 2)
myclick.shape("circle")
myclick.seth(0)

mydiapen2 = turtle.Turtle()
mydiapen2.color("white")
mydiapen2.penup()
mydiapen2.setposition(-350, -375)
mydiapen2.pendown()
mydiapen2.pensize(3)
mydiapen2.speed(0)

mypen.setx(350)
mypen.sety(375)
mypen.setx(-350)
mypen.sety(-375)

mypen.penup()
mypen.setpos(-350, 200)
mypen.pendown()
mypen.setx(350)

mypen.penup()
mypen.setx(100)
mypen.pendown()
mypen.sety(-375)

mydiapen.penup()
mydiapen.setpos(-125, -87.5)
Dialogue = "5"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(56.25)
Dialogue = "2"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(-231.25)
Dialogue = "8"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.setx(-237.5)
Dialogue = "7"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(-87.5)
Dialogue = "4"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(56.25)
Dialogue = "1"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.setx(-12.5)
Dialogue = "3"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(-87.5)
Dialogue = "6"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(-231.25)
Dialogue = "9"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))

mydiapen.setx(167.5)
Dialogue = "x"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(-87.5)
Dialogue = "+"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(56.25)
Dialogue = "c"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.setx(267.5)
Dialogue = "="
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(-87.5)
Dialogue = "-"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))
mydiapen.sety(-231.25)
Dialogue = "%"
mydiapen.write(Dialogue, False, align="left", font=("Arial", 25, "normal"))

#1
mydiapen.penup()
mydiapen.setpos(-268.5, 115)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#4
mydiapen.penup()
mydiapen.setpos(-268.5, -30)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#7
mydiapen.penup()
mydiapen.setpos(-268.5, -172)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#2
mydiapen.penup()
mydiapen.setpos(-157, 115)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#5
mydiapen.penup()
mydiapen.setpos(-157, -30)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#8
mydiapen.penup()
mydiapen.setpos(-157, -172)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#3
mydiapen.penup()
mydiapen.setpos(-43, 115)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#6
mydiapen.penup()
mydiapen.setpos(-43, -30)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#9
mydiapen.penup()
mydiapen.setpos(-43, -172)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)




#C
mydiapen.penup()
mydiapen.setpos(135.5, 115)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#=
mydiapen.penup()
mydiapen.setpos(245.5, 115)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#+
mydiapen.penup()
mydiapen.setpos(135.5, -28)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#-
mydiapen.penup()
mydiapen.setpos(245.5, -30)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#X
mydiapen.penup()
mydiapen.setpos(135.5, -175)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

#%
mydiapen.penup()
mydiapen.setpos(245.5, -175)
mydiapen.pendown()
mydiapen.seth(0)
mydiapen.fd(80)
mydiapen.seth(270)
mydiapen.fd(80)
mydiapen.seth(180)
mydiapen.fd(80)
mydiapen.seth(90)
mydiapen.fd(80)

mydiapen2.penup()
mydiapen2.setpos(-300, 287.5)
mypen.ht()
mydiapen.ht()
def clicked(x, y):
    myclick.goto(x, y)


sc.onscreenclick(clicked, 1)
turtle.listen()


global calculating
calculating = True
global btnclick
btnclick = False
global n1
n1 = "0"
global in_n1
in_n1 = True
global op
op = "+"
global in_op
in_op = False
global n2
n2 = "0"
global in_n2
in_n2 = False
global n1print
n1print = ""
global opprint
opprint = ""
global n2print
n2print = ""

global nprint
nprint = ""

def Calculatorapp():
    global in_n1
    global in_n2
    global n1print
    global n2print
    global op
    global nprint
    nprint = ""
    mydiapen2.clear()
    myclick.setposition(-350, -375)


    while calculating is True:
        myclick.speed(0)
        while in_n1 is True:
            if -268.5 < myclick.xcor() < -188.5 and 45 < myclick.ycor() < 115:
                nprint = "1"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -268.5 < myclick.xcor() < -188.5 and -110 < myclick.ycor() < -30:
                nprint = "4"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -268.5 < myclick.xcor() < -188.5 and -252 < myclick.ycor() < -172:
                nprint = "7"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -157 < myclick.xcor() < -77 and 45 < myclick.ycor() < 115:
                nprint = "2"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -157 < myclick.xcor() < -77 and -110 < myclick.ycor() < -30:
                nprint = "5"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -157 < myclick.xcor() < -77 and -252 < myclick.ycor() < -172:
                nprint = "8"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -43 < myclick.xcor() < 43 and 45 < myclick.ycor() < 115:
                nprint = "3"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -43 < myclick.xcor() < 43 and -110 < myclick.ycor() < -30:
                nprint = "6"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -43 < myclick.xcor() < 43 and -252 < myclick.ycor() < -172:
                nprint = "9"
                n1print += nprint
                mydiapen2.write(n1print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if 135 < myclick.xcor() < 215 and -108 < myclick.ycor() < -28:
                op = "+"
                in_n1 = False
                in_n2 = True
                myclick.setposition(-350, -375)
                mydiapen2.clear()

            if 135 < myclick.xcor() < 215 and -255 < myclick.ycor() < -175:
                op = "x"
                in_n1 = False
                in_n2 = True
                myclick.setposition(-350, -375)
                mydiapen2.clear()

            if 245.5 < myclick.xcor() < 325.5 and -108 < myclick.ycor() < -28:
                op = "-"
                in_n1 = False
                in_n2 = True
                myclick.setposition(-350, -375)
                mydiapen2.clear()

            if 245.5 < myclick.xcor() < 325.5 and -255 < myclick.ycor() < -175:
                op = "%"
                in_n1 = False
                in_n2 = True
                myclick.setposition(-350, -375)
                mydiapen2.clear()

            if 135 < myclick.xcor() < 215 and 35 < myclick.ycor() < 115:
                n1print = ""
                nprint = ""
                myclick.setposition(-350, -375)
                mydiapen2.clear()
            else:
                myclick.speed(0)


        while in_n2 is True:
            if -268.5 < myclick.xcor() < -188.5 and 45 < myclick.ycor() < 115:
                nprint = "1"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -268.5 < myclick.xcor() < -188.5 and -110 < myclick.ycor() < -30:
                nprint = "4"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -268.5 < myclick.xcor() < -188.5 and -252 < myclick.ycor() < -172:
                nprint = "7"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -157 < myclick.xcor() < -77 and 45 < myclick.ycor() < 115:
                nprint = "2"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -157 < myclick.xcor() < -77 and -110 < myclick.ycor() < -30:
                nprint = "5"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -157 < myclick.xcor() < -77 and -252 < myclick.ycor() < -172:
                nprint = "8"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -43 < myclick.xcor() < 43 and 45 < myclick.ycor() < 115:
                nprint = "3"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -43 < myclick.xcor() < 43 and -110 < myclick.ycor() < -30:
                nprint = "6"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if -43 < myclick.xcor() < 43 and -252 < myclick.ycor() < -172:
                nprint = "9"
                n2print += nprint
                mydiapen2.write(n2print, False, align="left", font=("Arial", 25, "normal"))
                myclick.setposition(-350, -375)

            if 135 < myclick.xcor() < 215 and 35 < myclick.ycor() < 115:
                n1print = ""
                n2print = ""
                nprint = ""
                myclick.setposition(-350, -375)
                mydiapen2.clear()
                in_n2 = False
                in_n1 = True

            if 245.5 < myclick.xcor() < 325.5 and 35 < myclick.ycor() < 115:
                in_n2 = False
                myclick.setposition(-350, -375)
                mydiapen2.clear()
                Calculate()
            else:
                myclick.speed(0)


def Calculate():
    global n1print
    global n2print
    global in_n1
    global in_n2
    global op
    global show
    n1print = float(n1print)
    n2print = float(n2print)
    final = 0
    float(final)
    show = True
    if op == "+":
        final = n1print + n2print
        mydiapen2.write(final, False, align="left", font=("Arial", 25, "normal"))

    if op == "x":
        final = n1print * n2print
        mydiapen2.write(final, False, align="left", font=("Arial", 25, "normal"))

    if op == "-":
        final = n1print - n2print
        mydiapen2.write(final, False, align="left", font=("Arial", 25, "normal"))

    if op == "%":
        final = n1print / n2print
        mydiapen2.write(final, False, align="left", font=("Arial", 25, "normal"))

    while show is True:
        myclick.speed(0)
        if 135 < myclick.xcor() < 215 and 35 < myclick.ycor() < 115:
            show = False
            n1print = ""
            n2print = ""
            in_n1 = True
            Calculatorapp()

        if 135 < myclick.xcor() < 215 and -108 < myclick.ycor() < -28:
            op = "+"
            in_n1 = False
            in_n2 = True
            n1print = final
            n2print = ""
            myclick.setposition(-350, -375)
            mydiapen2.clear()
            show = False
            Calculatorapp()

        if 135 < myclick.xcor() < 215 and -255 < myclick.ycor() < -175:
            op = "x"
            in_n1 = False
            in_n2 = True
            n1print = final
            n2print = ""
            myclick.setposition(-350, -375)
            mydiapen2.clear()
            show = False
            Calculatorapp()

        if 245.5 < myclick.xcor() < 325.5 and -108 < myclick.ycor() < -28:
            op = "-"
            in_n1 = False
            in_n2 = True
            n1print = final
            n2print = ""
            myclick.setposition(-350, -375)
            mydiapen2.clear()
            show = False
            Calculatorapp()

        if 245.5 < myclick.xcor() < 325.5 and -255 < myclick.ycor() < -175:
            op = "%"
            in_n1 = False
            in_n2 = True
            n1print = final
            n2print = ""
            myclick.setposition(-350, -375)
            mydiapen2.clear()
            show = False
            Calculatorapp()

Calculatorapp()
turtle.done()
