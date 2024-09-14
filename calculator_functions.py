ads = int(input("welcome to the calculator project please enter the number for the corresponding operation\n 1.Addition \n 2Subtraction \n3.Multiplication\n4.division\n5.remainder\n6.quotient : "))
def addition(x, y):
  return x+y

def subtraction(x, y):
  return x-y

def multiplication(x, y):
  return x*y

def division(x, y):
 return x/y

def quotient(x, y):
  return x//y

def remainder(x, y):
  return x%y

if ads == 1:
  rty = float(input("Please enter your first  number : "))
  rby = float(input("Please enter your second  number : ")) 
  print(addition(rty, rby))
  
elif ads == 2:
  rty = float(input("Please enter your first  number : "))
  rby = float(input("Please enter your second  number : ")) 
  print(subtraction(rty, rby))

elif ads == 3:
  rty = float(input("Please enter your first  number : "))
  rby = float(input("Please enter your second  number : ")) 
  print(multiplication(rty, rby))


elif ads == 4:
  rty = float(input("Please enter your first  number : "))
  rby = float(input("Please enter your second  number : ")) 
  print(division(rty, rby))


elif ads == 5:
  rty = float(input("Please enter your first  number : "))
  rby = float(input("Please enter your second  number : ")) 
  print(remainder(rty, rby))

elif ads == 6:
  rty = float(input("Please enter your first  number : "))
  rby = float(input("Please enter your second  number : ")) 
  print(quotient(rty, rby))

  
  

type(ads)
