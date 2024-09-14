q1 = int(input("please enter a number : ")) #123
c = 0
n2 = q1

while n2 > 0:
  n1 = n2 % 10
  c = (c * 10) + n1
  n2 = n2 // 10

if q1 == c:
  print("It is a palindrome number")

else:
  print("It is not a palindrome number")