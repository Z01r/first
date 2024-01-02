import turtle
import random


def Tri(n):
    turtle.forward(n)
    turtle.right(-60)
    turtle.forward(n)
    turtle.right(-60)
    turtle.forward(n)
    return 0


n = int(input())
print(Tri(n))
turtle.speed(100)
k = ['green', 'white', 'black', 'blue', 'yellow', 'red']
while 1 != 2:
    turtle.bgcolor(k[random.randrange(0, len(k))])
    n += 1
    turtle.pencolor(k[random.randrange(0, len(k))])
    turtle.forward(10 * (random.randrange(0, len(k))))
    turtle.right(180)
    turtle.forward(10 * (random.randrange(0, len(k))))
    turtle.right(n + 1)
    turtle.circle(random.randrange(0, 100))
