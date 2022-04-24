# The flower pattern
import turtle
from math import cos, sin
window = turtle.Screen()
shapes = turtle.Turtle()
draw = turtle.Turtle()
shapes.pensize(1)
shapes.speed(0)
shapes.color("#999999")

draw.pensize(1)
draw.speed(0)
shapes.color("#000000")



def triangle(size, turtle1, turtle2):
    turtle1.penup()
    for t in range(0, 3):
        turtle1.fd(size)
        turtle1.right(120)
        x = turtle1.xcor()
        y = turtle1.ycor()
        turtle2.penup()
        turtle2.goto(x-size, y)
        turtle2.seth(270)
        turtle2.pendown()
        if(t == 2):
            turtle2.color("#ffffff")
        else:
            turtle2.color("#000000")
        turtle2.circle(size)
    turtle1.pendown()
        
def waves(size, turtle1):
    for t in range(0, 6):
        turtle1.fd(size)
        turtle1.right(145)

for s in range(50, 100):
    for t in range(0, 3):
        triangle(1*s, shapes, draw)
        shapes.right(120)

turtle.exitonclick()