from random import randint
import turtle as t
import numpy as np
screen = t.Screen()
screen.setup(500,500)
screen.title("C18001242")
pen = t.Turtle()
#ve hinh vuong
# pen.penup()
# pen.goto(-100,100)
# pen.pendown()
# for i in range(4):
#     pen.left(90)
#     pen.fd(100)
# #ve hinh tam giac
# pen.penup()
# pen.goto(100,100)
# pen.pendown()
# for i in range(3):
#     pen.fd(100)
#     pen.left(120)
# #ve hinh tron
# pen.penup()
# pen.goto(-150,-100)
# pen.pendown()
# pen.circle(50)
# pen.penup()
# pen.goto(150,-100)
# pen.pendown()
# pen.shape("turtle")
# t.bgcolor("green")
# #pen.pensize(5)
# #pen.bk(100)
# pen.shapesize(3,3,3)
# pen.fillcolor("white")
# pen.pencolor("red")
# pen.bk(100)

colours = ["Red","Blue","Yellow","Black","Green","Pink","Orange"]
all_turtles = []
for num in range (1,7):
    t_turtle = t.Turtle()
    t_turtle.shape("turtle")
    t_turtle.color(colours[num])
    t_turtle.penup()
    t_turtle.goto(-220, -100 + 30 * num)
    all_turtles.append(t_turtle)
n = len(all_turtles)
for j in range(70):
    for i in range(n):
        all_turtles[i].forward(randint(1,10))
#ve nha`
pen.penup()
pen.goto(100,0)
pen.pendown()
pen.color('black','green')
pen.begin_fill()
for i in range(4):
    pen.fd(100)
    pen.right(90)
pen.end_fill()
pen.color('black','blue')
pen.begin_fill()
for i in range(3):
    pen.fd(100)
    pen.left(120)
pen.end_fill()
pen.penup()
pen.goto(100,100)
pen.pendown()
pen.color('black','orange')
pen.begin_fill()
pen.circle(50)
pen.end_fill()
screen.exitonclick()







