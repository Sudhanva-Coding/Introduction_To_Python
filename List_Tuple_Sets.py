abc =[12, "Sudhanva", True, 39.23, "Hey there", False]
#print(type(abc))

if type(abc) is list:
  print("abc is a list")
elif type(abc) is tuple:
  print("abc is a tuple")
elif type(abc) is set:
  print("abc is a set")

else:
  print("abc is neither list or tuple or sets")