from turtle import Turtle, Screen
from random import randint

screen = Screen()
tim = Turtle()
tim.shape('turtle')
tim.color('blue violet')
screen.colormode(255)
for i in range(3,11):
    turn = 360/i
    tim.pencolor(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
    for x in range(i):
        tim.right(turn)
        tim.forward(100)
























screen.exitonclick()