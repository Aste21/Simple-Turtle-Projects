import turtle
from random import randint

turtle.colormode(255)
screen = turtle.Screen()
tim = turtle.Turtle()
tim.speed('fastest')

for x in range(60):
    tim.pencolor(randint(0, 255),
                 randint(0, 255),
                 randint(0, 255))
    tim.circle(100)
    tim.right(6)

screen.exitonclick()