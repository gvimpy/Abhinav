import turtle 
import time
print ("Copyright Abhinav Elimineti")
Abhinav = turtle.Turtle()
def Left():
    Abhinav.setheading (180)
    Abhinav.forward(50)
def Right():
    Abhinav.setheading (-180)
    Abhinav.backward(50)
def Increase_pen_size():
    Abhinav.shapesize(12) #Copyright Abhinav Elimineti
    Abhinav.pensize(11)
def Pensize_normal():
    Abhinav.shapesize(1)
    Abhinav.pensize(1)
def Hide_Turtle():
    Abhinav.hideturtle()
def Im_back():
    Abhinav.showturtle()
def Erase():
    Abhinav.clear()
def Shape_shift():
    Abhinav.shape ("turtle")
def Shapey_shift_back():
    Abhinav.shape ("arrow")
def Up():
    Abhinav.setheading (90)
    Abhinav.forward (50)
def Down():
    Abhinav.setheading (270)
    Abhinav.forward (50)
def BackgroundColor():
    turtle.bgcolor ("Blue")
def Credits(x, y):
    Abhinav.write ("Made by Abhinav Elimineti")
turtle.listen()
Abhinav.shape("arrow")
turtle.onkey(Left, "Left")
turtle.onkey(Right, "Right")
turtle.onkey(Increase_pen_size, "S")
turtle.onkey(Pensize_normal, "b")
turtle.onkey(Hide_Turtle, "1")
turtle.onkey(Im_back, "2")
turtle.onkey(Erase, "e")
turtle.onkey(Shape_shift, "t")
turtle.onkey(Shapey_shift_back, "w")
turtle.onkey (Up, "Up")
turtle.onkey (Down, "Down")
turtle.onkey (BackgroundColor, "c")
turtle.onscreenclick (Credits, 1)
turtle.title("Not Abhinav Paint")
Type = input("Text:")
Abhinav.write(Type)
time.sleep (0.1)
Abhinav.hideturtle()
time.sleep (2)
Abhinav.showturtle()
turtle.mainloop()