ads = int(input("Please enter a number : ")) #186 
c = 0
n1 = ads


while (n1 > 0):
  n2 = n1 % 10
  c += n2 ** 3
  n1  = n1 // 10

if c == ads:
  print("This is an armstrong number")

else:
  print("this is not an armstrong number")
  