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

game = [rock, paper, scissors]

# get user's choice; 0,1 or 2
user_choice = int(input("Rock [0], Paper [1], or Scissors [2]?\n"))
print(game[user_choice])

computer_choice = random.randint(0, 2)
print(f"The computer chose:\n {game[computer_choice]}")

if user_choice > 2 or user_choice < 0:
    print("Invalid choice!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a tie!")
