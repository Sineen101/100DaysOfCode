import random

logo = """
    //   ) )                                           //   ) )                              
   //                  ___      ___      ___          //         ___      _   __      ___    
  //  ____  //   / / //___) ) ((   ) ) ((   ) )      //  ____  //   ) ) // ) )  ) ) //___) ) 
 //    / / //   / / //         \ \      \ \         //    / / //   / / // / /  / / //        
((____/ / ((___( ( ((____   //   ) ) //   ) ) ()()(|(____/ / ((___( ( // / /  / / ((____     
"""


def attempts(guess, number, turns):
    """This function will check if the guess is correct and will return the number of attempts remaining"""
    continue_game = True
    while continue_game:
        if guess > number:
            print("Too high!")
            return turns - 1
        elif guess < number:
            print("Too low!")
            return turns - 1
        elif guess == number:
            print(f"You got it! The number was {number}")
            continue_game = False


def difficulty():
    """Sets the number of attempts based on the difficulty"""
    level = input("Choose a level: easy, medium, hard: ")
    if level == "easy":
        return 10
    elif level == "medium":
        return 6
    elif level == "hard":
        return 3


def game():
    """This function runs the game"""
    print(logo+"\n`````````````Guessing Game`````````````\nI'm thinking of a number between 1 and 100.\nTry to guess it in as few attempts as possible.\n")
    number = random.randint(1, 100)
    turns = difficulty()
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts left!")
        guess = int(input("Guess a number: "))
        turns = attempts(guess, number, turns)
        if turns == 0:
            print("You lost the game. The number was {}".format(number))
            return
        elif guess != number:
            print("Try again!")


game()
