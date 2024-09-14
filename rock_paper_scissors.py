import random
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

while True:
  print("Enter choice : \n1. For Rock, \n2. For Paper, \n3. For Scissors")
  abc = int(input("Enter your input : "))
  while (abc < 1) or (abc > 3):
    abc = int(input("Enter a valid input between 1-3: "))

  if abc == 1:
    choice_name = "Rock"
  elif abc == 2:
    choice_name = "Paper"
  else:
    choice_name = "Scissors"

  print("User choice is :", choice_name)
  print("\nNow it's computer's turn ...")

  fgh = random.randint(1,3)

  if fgh == 1:
    computer_choice_name = "Rock"
  elif abc == 2:
    computer_choice_name = "Paper"
  else:
    comuter_choice_name = "Scissors"

  print("Computer choice is :", computer_choice_name)
  print("\n", choice_name, " V/s ", computer_choice_name)
  if((abc == 1 and fgh == 2) or (abc == 2 and fgh == 1)):
    print("paper wins => ", end = "")
    result = "paper"
    
  elif((abc == 2 and fgh == 3) or (abc == 3 and fgh == 2)):
    print("Scissor wins => ", end = "")
    result = "Scissor"

  else:
    print("Rock wins => ", end = "")
    result = "Rock"

  if result == choice_name:
    print("<== User wins ==>")
  else:
    print("<== Computer wins ==>")
         
  print("Do you want to play again? (Y/N)")
  ans = input()

  if ans == 'n' or ans == 'N':
    break

print("\nThanks for Playing!")
  


  

    
  

  
  