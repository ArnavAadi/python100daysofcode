import os
import random

import art

os.system('cls')

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_playing = input("you want to play blacjack: ")


while "y" in is_playing:
    print(art.logo)

    def calculate_score(fcards):
        score = sum(fcards)
        if score == 21:
            return 0
        elif score > 21:
            if 11 in fcards:
                fcards.remove(11)
                fcards.append(1)
                score = sum(fcards)
                return score
            else:
                return score
        else:
            return score

    def card_drawer():
        return random.choice(cards)

    player_cards = [card_drawer(), card_drawer()]
    computer_cards = [card_drawer(), card_drawer()]
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your Cards: {player_cards}, current score: {player_score}")
    print(f"computer's first card: {computer_cards[0]}")

    def player_checker(pl_score, pl_cards):
        if computer_score == 0 or pl_score > 21:
            print("you lose")
        elif pl_score == 0:
            print("you win")
        else:
            draw_card = input("do you want to draw a card: ")
            if "y" in draw_card:
                player_cards.append(card_drawer())
                pl_score = calculate_score(pl_cards)
                print(f"Your cards: {pl_cards}, current score: {pl_score}")
                player_checker(pl_score, pl_cards)
            elif "n" in draw_card:
                print(
                    f"Your final hand: {pl_cards}, current score: {pl_score}")
                computer_checker(computer_score, computer_cards, pl_score)

    def computer_checker(co_score, co_cards, pl_score):
        if co_score < 17:
            computer_cards.append(card_drawer())
            co_score = calculate_score(co_cards)
            computer_checker(co_score, co_cards, pl_score)
        elif co_score > 21:
            print(
                f"Computer's final hand: {co_cards}, Final score: {co_score}")
            print("you win")
        else:
            print(
                f"Computer's final hand: {co_cards}, Final score: {co_score}")
            compare(co_score, pl_score)

    def compare(co_scr, pl_scr):
        if co_scr == pl_scr:
            print("thats a draw")
        elif pl_scr > co_scr:
            print("you win")
        else:
            print("you lose")

    player_checker(player_score, player_cards)
    is_playing = input("you want to play blacjack: ")
    os.system('cls')
