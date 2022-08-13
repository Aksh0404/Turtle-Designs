import turtle
colors = ['red','yellow','pink','blue','orange','purple']
y = turtle.Pen()
turtle.bgcolor("black")
for x in range(300):
    y.pencolor(colors[x%6])
    y.backward(x)
    y.width(x//100+1)
    y.right(50)
    
