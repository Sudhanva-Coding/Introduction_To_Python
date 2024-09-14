import turtle,random
ard = turtle.Turtle()
ads = turtle.Screen()
ads.bgcolor("indigo")
ard.pensize(3)
ard.speed(100)

for i in range (15):
  x = random.randint(0, 500)
  y = random.randint(0, 500)
  ard.pencolor("lightgreen")
  ard.fillcolor("lightgreen")
  ard.penup()
  ard.goto(x,y)
  ard.pendown()
  count = 0
  ard.begin_fill()
  while count < 6:
    ard.forward(100)
    ard.left(144)
    count = count+1
  ard.end_fill()
  ard.right(45)