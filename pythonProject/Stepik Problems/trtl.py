import turtle

n = 0
k = ['Мама', 'Ты', 'Самая', 'Лучшая']
turtle.speed(1)
h = ['red', 'green']
for i in range(4):
    turtle.bgcolor(h[i % 2])
    turtle.write(k[i])

