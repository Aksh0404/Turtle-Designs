import turtle
colors = ['red','purple','blue','pink','yellow','orange']
t=turtle.Turtle()
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)
