import turtle
from random import randint

turtle.colormode(255)
screen = turtle.Screen()
tim = turtle.Turtle()
tim.pensize(7)
tim.speed('fastest')
for x in range(1000):
    direction = randint(0,3)
    tim.pencolor(randint(0, 255),
                 randint(0, 255),
                 randint(0, 255))
    if direction == 0:
        tim.right(90)
    elif direction == 1:
        tim.left(90)
    elif direction == 2:
        tim.right(180)
    tim.forward(20)



















screen.exitonclick()