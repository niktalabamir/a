import turtle

turtle.pencolor("cyan")
turtle.bgcolor("pink")
turtle.speed(20)
turtle.right(45)
for i in range(150):
    if 7 < i < 62:
        turtle.left(5)
    if 80 < i <133 :
        turtle.right(5)
    turtle.circle(90)
    if i < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)
turtle.pencolor("red")
turtle.bgcolor("white")
turtle.speed(20)
turtle.right(45)
for n in range(150):
    if 7 < n < 62:
        turtle.left(5)
    if 80 < n <133 :
        turtle.right(5)
    turtle.circle(60)
    if n < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)
turtle.pencolor("blue")
turtle.bgcolor("green")
turtle.speed(20)
turtle.right(45)
for w in range(150):
    if 7 < w < 62:
        turtle.left(5)
    if 80 < w <133 :
        turtle.right(5)
    turtle.circle(40)
    if w < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)

turtle.pencolor("green")
turtle.bgcolor("black")
turtle.speed(20)
turtle.right(45)
for h in range(150):
    if 7 < h < 62:
        turtle.left(5)
    if 80 < h <133 :
        turtle.right(5)
    turtle.circle(50)
    if h < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)
turtle.done()