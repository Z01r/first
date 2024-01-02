import random
import turtle
turtle.pen('turtle')

turtle.speed(100)
a = ['blue','cyan','deepskyblue','aqua','steelblue']
while 1 != 2:
    turtle.bgcolor(a[random.randrange(0,5)])
    turtle.forward(200)
    turtle.right(180)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(180)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(180)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(180)
    turtle.forward(200)
    turtle.right(45)
    turtle.circle(random.randrange(0,200))
