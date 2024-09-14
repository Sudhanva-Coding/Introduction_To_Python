abc1 = 29
#print(abc1)
print(type(abc1))

abc2 = 36.13
print(type(abc2))

abc3 = "Sudhanva"  "1999"
print(type(abc3))

abc4 = 13 < 19
print(type(abc4))

abc1 = float(29)
print(type(abc1))
print(abc1)


print(abc1)
print(type(abc1))

abc4 = str(13 < 19)
print(type(abc4))
print(abc4)

# write a program to calculate if an individual is eligible to vote : if he is less than 10 display as kid, from 10 to 17 display teenager, 18 and above adult and eligible to vote
# 10 <= ret1 <= 17
# == != >= <= = < >

ret1 = int(input("How old are you : "))

if ret1 < 10 and ret1 >-1:
  print("You are a kid")
elif (ret1 >= 10) and (ret1 <=17):
  print("You are a teenager")
elif (ret1 >=  18):
  print("You are an adult and eligible to vote")
else:
 print ("Please enter a valid integer")



#print(class(abc2))




