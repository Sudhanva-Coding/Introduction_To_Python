import turtle
abc = turtle.Turtle()

ytr = turtle.Screen()

jrd = 0
#rte = 0
#lkj = 0  
#sti = 0

lkj = input("Please choose background color : ")
print(lkj)
ytr.bgcolor(lkj)

qwe = input ("Please select pen color :" )
abc.color(qwe)

while jrd < 36:
  abc.forward(17)
  abc.right(10)
  jrd = jrd + 1

jrd = 0
while jrd < 36:
  abc.left(10)
  abc.forward(12)
  jrd += 1
abc.penup()
abc.goto(0,228)
abc.pendown()

jrd = 0
while jrd < 36:
  abc.forward(8)
  abc.right(10)
  jrd += 1
  
# Draw eyes of snowman
abc.penup()
abc.goto(-15,200)
abc.pendown()
abc.circle(4)

abc.penup()
abc.goto(22,200)
abc.pendown()
abc.circle(4)

# Draw smile of Snowman
abc.penup()
abc.goto(-15, 175)
abc.pendown()
abc.right(90)

jrd = 0
while jrd < 18:
  abc.forward(4)
  abc.left(10)
  jrd += 1
  


abc.hideturtle()
