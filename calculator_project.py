# if (xec%2 == 0):
#   print("This is an even number")
#print(21/2) 

def Add(P, Q):
  return P+Q

def minus(x, z):
  return x-z

def times(w, r):
  return w*r

def divide(x, z):
  return x/z

def remainder(x, z):
  return x%z

def quotient(p, q):
  return p//q

print("Welcome to the calculator project")
print("Select an operation to proceed: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Quotient \n6. Remainder")

ret = int(input("\nPlease Choose an option : "))

tre = int(input("Please enter the first number : "))
qwe = int(input("Please enter the second number : "))

if  ret == 1:
  print("The result of Addition is : ", Add(tre, qwe))
  
elif  ret == 2:
  print("The result of Subtraction is : ", minus(tre, qwe))

elif  ret == 3:
  print("The result of Multiplication is : ", times(tre, qwe))

elif  ret == 4:
  print("The result of Division is : ", divide(tre, qwe))

elif  ret == 6:
  print("The result of Remainder  is : ", remainder(tre, qwe))

elif  ret == 5:
  print("The result of Quotient is : ", quotient(tre, qwe))