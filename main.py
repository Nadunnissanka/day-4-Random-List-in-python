import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock paper siccors!")
print("------------------------------")

game_images = [rock, paper, scissors]
player_option = int(input("What do you choose? Rock - 0 , Paper - 1 and Scissors - 2: "))

if player_option == 0:
  print(game_images[0])
  comp_opt = random.randint(0,2)
  if comp_opt == 0:
    print("\nComputer Choose:\n")
    print(game_images[0])
    print("\nDraw!!")
  elif comp_opt == 1:
    print("\nComputer Choose:\n")
    print(paper)
    print("\nComputer Won!!")
  else:
    print("\nComputer Choose:\n")
    print(scissors)
    print("\nPlayer Won!!")
elif player_option == 1:
  print(paper)
  comp_opt = random.randint(0,2)
  if comp_opt == 0:
    print("\nComputer Choose:\n")
    print(rock)
    print("\nPlayer Won!!")
  elif comp_opt == 1:
    print("\nComputer Choose:\n")
    print(paper)
    print("\nDraw!!")
  else:
    print("\nComputer Choose:\n")
    print(scissors)
    print("\nComputer Won!!")
elif player_option == 2:
  print(scissors)
  comp_opt = random.randint(0,2)
  if comp_opt == 0:
    print("\nComputer Choose:\n")
    print(rock)
    print("\nComputer Won!!")
  elif comp_opt == 1:
    print("\nComputer Choose:\n")
    print(paper)
    print("\nPlayer Won!!")
  else:
    print("\nComputer Choose:\n")
    print(scissors)
    print("\nDraw!!")
else:
  print("Invalid Input!")