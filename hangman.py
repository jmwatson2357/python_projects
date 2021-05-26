import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

# print(f'Pssst, the solution is {chosen_word}.')

display = []
already_guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if not already_guessed.count(guess) == 0:
        print(f"You have already guessed {guess}")
    else:
        already_guessed += guess
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])