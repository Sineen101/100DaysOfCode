import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

print(logo)  # print logo

chosen_word = random.choice(word_list)  # random word from the list

clear()  # clear the screen

display = []  # list of underscores
for i in range(len(chosen_word)):
    display.append("_")
print(display)  # print the list of underscores


end_of_game = False  # boolean variable to check if the game is over
lives = 6  # number of lives
while not end_of_game:
    guess = input("Guess a letter: ").lower()  # user input to guess the word

    if guess in display:    # if the letter is already in the list of underscores
        print("You already guessed that letter")

    # loop to check if the letter is in the word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            # if the letter is in the word, replace the underscore with the letter
            display[position] = letter

    if guess not in chosen_word:
        # if the letter is not in the word, print this message
        print("Wrong guess! You lose a life!")
        lives -= 1  # lose a life
        if lives == 0:
            print("You lost! The word was: " + chosen_word)
            end_of_game = True  # end the game

    # print the list of underscores with the letters replaced
    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You won!")
        end_of_game = True

    print(stages[lives])    # print the stages of the hangman game
