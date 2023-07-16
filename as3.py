import turtle

turtle.pencolor("cyan")
turtle.bgcolor("pink")
turtle.speed(11)
turtle.right(45)
for n in range(150):
    if 7 < n < 62:
        turtle.left(5)
    if 80 < n <133 :
        turtle.right(5)
    turtle.circle(90)
    if n < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)
turtle.pencolor("red")
turtle.bgcolor("white")
turtle.speed(11)
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
turtle.bgcolor("pink")
turtle.speed(11)
turtle.right(45)
for n in range(150):
    if 7 < n < 62:
        turtle.left(5)
    if 80 < n <133 :
        turtle.right(5)
    turtle.circle(40)
    if n < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)

turtle.pencolor("green")
turtle.bgcolor("plack")
turtle.speed(11)
turtle.right(45)
for n in range(150):
    if 7 < n < 62:
        turtle.left(5)
    if 80 < n <133 :
        turtle.right(8)
    turtle.circle(50)
    if n < 70:
        turtle.forward(10)
    else:
        turtle.forward(5)
turtle.done()