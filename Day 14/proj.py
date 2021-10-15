import random
import art
import game_data
import os

score = 0
a = random.choice(game_data.data)
b = random.choice(game_data.data)

is_playing = True
while is_playing:
    os.system("cls")
    print(art.logo)
    print(f"current score: {score}")
    b = random.choice(game_data.data)
    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']}, {b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    winner = ""
    starter = a
    if a['follower_count'] > b['follower_count']:
        winner = 'a'
        starter = a
    else:
        winner = 'b'
        starter = b

    if answer == winner:
        score += 1
        a = starter
    else:
        print("thats wrong")
        print(f"your score is {score}")
        is_playing = False
