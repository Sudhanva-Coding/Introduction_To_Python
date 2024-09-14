import turtle, random
ads = turtle.Turtle()
bda = turtle.Screen()
bda.bgcolor("black")
ads.speed(100)
ads.pensize(3)

for i in range (15):
  x = random.randint(0, 500)
  y = random.randint(0, 500)
  ads.penup()
  ads.goto(x,y)
  ads.pendown()
  i = 36
  ads.color("red")
  while i > 0:
    i = i-1
    a = random.randint(20, 40)
    ads.forward(a)
    ads.backward(a)
    ads.left(10)    