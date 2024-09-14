import turtle
pen = turtle.Turtle()
pen.pensize(5)
ert = input("What shape would you like to draw circle, triangle or square : ").lower()

if ert == "square":
  print("You have chosen square")
  for i in range(4):
    pen.forward(200)
    pen.right(90)

elif ert == "circle":
  print ("you have chosen circle")
  for i in range(36):
    pen.forward(10)
    pen.right(10)

elif ert == "triangle":
  print("you have chosen triangle")
  for i in range (3):
    pen.forward(100)
    pen.left(120)