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

action = int(
    input("select a number 0 for rock, 1 for paper, 2 for scissors   : \n"))

computer = random.randint(0, 2)

if action == 0:
    print(rock)

elif action == 1:
    print(paper)
elif action == 2:
    print(scissors)
else:
    print("not valid")

print("computer's choice")

if computer == 0:
    print(rock)

elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if action == 0 and computer == 1 or action == 1 and computer == 2 or action == 2 and computer == 0:
    print("you lose")
elif action == computer:
    print("its a draw")
else:
    print("you win")
