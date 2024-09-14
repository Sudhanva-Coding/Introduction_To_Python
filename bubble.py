# import turtle, random
# ads = turtle.Turtle()
# bda = turtle.Screen()
# bda.bgcolor("yellow")
# ads.speed(100)
# ads.pensize(6)
# speed = 100

# for i in range (15):
#   x = random.randint(0, 350)
#   y = random.randint(0, 350)
#   ads.penup()
#   ads.goto(x,y)
#   ads.pendown()
#   i = 36
#   ads.color("blue")
#   while i > 0:
#     a = random.randint(15, 40)
#     ads.forward(a)
#     #ads.backward(a)
#     ads.left(10)
#     i = i-1



import turtle
import random

t = turtle.Turtle()
t.pensize(3)
t.speed(40)

screen = turtle.Screen()
screen.bgcolor("sky blue")

for i in range(15):
  x = random.randint(-500,500)
  y = random.randint(-500,500)
  t.penup()
  t.goto(x,y)
  t.pendown()
  
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)

  t.pencolor("lightgreen")
  t.fillcolor("lightgreen")

  t.begin_fill()
  a = random.randint(50,100)
  t.circle(a)
  t.end_fill()