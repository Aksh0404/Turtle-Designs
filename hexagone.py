import turtle
colors = ['red', 'yellow', 'blue', 'pink', 'green', 'purple']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(1000)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)