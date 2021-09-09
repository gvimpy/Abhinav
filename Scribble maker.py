import turtle
import time
Lala = turtle.Turtle ()
def Abhinav ():
    Lala.forward (50)
def bhinav ():
    Lala.backward (100)
def lalai ():
    Lala.setheading (90)
    Lala.forward (100)
def ii ():
    Lala.setheading (270)
    Lala.forward (100)
def yuyu ():
    Lala.setheading (-270)
def r ():
    Lala.setheading (-90)
Lala.shape ("turtle")
turtle.listen ()
turtle.onkey (bhinav, "Left")
turtle.onkey (Abhinav, "Right")
turtle.onkey (lalai, "Up")
turtle.onkey (ii, "Down")
turtle.onkey (yuyu, "?")
turtle.onkey (r, "Tab")
turtle.mainloop ()