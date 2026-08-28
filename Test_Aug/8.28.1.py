import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.color("white")

for i in range(80):
    x = random.randint(-300,300)
    y = random.randint(-250,250)

    star.penup()
    star.goto(x,y)
    star.dot(random.randint(2,5))

    turtle,done()