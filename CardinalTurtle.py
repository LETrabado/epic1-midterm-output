#Cardinal Turtle class showcase
import turtle
import random
window = turtle.Screen()

#The Cardinal turtle class
class Cardinal:
    north = turtle.Turtle()
    east = turtle.Turtle()
    south = turtle.Turtle()
    west  = turtle.Turtle()

    north.hideturtle()
    east.hideturtle()
    south.hideturtle()
    west.hideturtle()
    
    #set heading to different directions
    north.seth(90)
    east.seth(0)
    south.seth(270)
    west.seth(180)

    north.speed(0)
    east.speed(0)
    south.speed(0)
    west.speed(0)

    north.color("#000000")
    east.color("#000000")
    south.color("#000000")
    west.color("#000000")
#turtle functions edited to fit 4 turtles
    def forward(distance):
        Cardinal.north.fd(distance)
        Cardinal.east.fd(distance)
        Cardinal.south.fd(distance)
        Cardinal.west.fd(distance)

    def right(angle):
        Cardinal.north.right(angle)
        Cardinal.east.right(angle)
        Cardinal.south.right(angle)
        Cardinal.west.right(angle)

    def penup():
        Cardinal.north.penup()
        Cardinal.east.penup()
        Cardinal.south.penup()
        Cardinal.west.penup()

    def pendown():
        Cardinal.north.pendown()
        Cardinal.east.pendown()
        Cardinal.south.pendown()
        Cardinal.west.pendown()

    def goto(x, y):
        Cardinal.north.goto(x, y)
        Cardinal.east.goto(y, 0-x)
        Cardinal.south.goto(0-x, 0-y)
        Cardinal.west.goto(0-y, x)

    def seth(angle):
        Cardinal.north.seth(angle + 90)
        Cardinal.east.seth(angle)
        Cardinal.south.seth(angle + 270)
        Cardinal.west.seth(angle + 180)

    def circle(size):
        Cardinal.north.circle(size)
        Cardinal.east.circle(size)
        Cardinal.south.circle(size)
        Cardinal.west.circle(size)

    def color(pen, cover):
        Cardinal.north.color(pen, cover)
        Cardinal.east.color(pen, cover)
        Cardinal.south.color(pen, cover)
        Cardinal.west.color(pen, cover)

    def begin_fill():
        Cardinal.north.begin_fill()
        Cardinal.east.begin_fill()
        Cardinal.south.begin_fill()
        Cardinal.west.begin_fill()

    def end_fill():
        Cardinal.north.end_fill()
        Cardinal.east.end_fill()
        Cardinal.south.end_fill()
        Cardinal.west.end_fill()
#uses random module to test the class
draw = Cardinal
for t in range(0, random.randint(1, 3)):
    draw.seth(random.randint(0, 360))
    draw.forward(random.randint(50, 100))
    draw.right(random.randint(0, 360))
    draw.goto(random.randint(-100, 100), random.randint(0, 100))
    draw.circle(random.randint(10, 100))


turtle.exitonclick()