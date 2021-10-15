import random

difficulty = input("choose the difficulty hard or easy: ")

if difficulty == "hard":
    difficulty = 5
else:
    difficulty = 10

print(f"you have {difficulty} guesses")
number = random.randint(1, 100)

while difficulty != 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
    difficulty -= 1
    print(f"you have {difficulty} turns.")
