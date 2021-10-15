import random
import hangman_art
import hangman_word

print(hangman_art.logo)
chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"you have already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"you guessed {guess} thats not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
    if lives == 0:
        print(f'word was : {chosen_word}')
