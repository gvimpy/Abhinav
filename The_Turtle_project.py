import turtle 
Abhinav = turtle.Turtle()
def Variable1():
    Abhinav.forward(100)
def Variable2():
    Abhinav.backward(100)
def Variable3():
    Abhinav.shapesize(12)
    Abhinav.pensize(11)
def Variable4():
    Abhinav.shapesize(1)
    Abhinav.pensize(1)
def Variable5():
    Qwerty = turtle.Turtle()
    def Inside1():
       Qwerty.forward(100) 
    def Inside2():
        Qwerty.backward(100)
    turtle.onkey (Inside1, "W")
    turtle.onkey (Inside2, "S")
turtle.listen()
Abhinav.shape ("arrow")
turtle.onkey (Variable1, "Up")
turtle.onkey (Variable2, "Down")
turtle.onkey (Variable3, "Right")
turtle.onkey (Variable4, "Left")
turtle.onkey (Variable5, "C")
turtle.title ("Abhinav Paint")
turtle.mainloop()