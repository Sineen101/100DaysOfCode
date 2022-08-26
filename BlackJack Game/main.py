import random
import os


logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""


def clear():    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    """This function deals a card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    """This function calculates the score of the player or the dealer"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(player_score, dealer_score):
    """This function compares the scores of the player and the dealer"""
    if player_score == dealer_score:
        print("It is a tie! The computer has won!")
    elif player_score == 0 and dealer_score == 0:
        return "Tie with a blackjack"
    elif dealer_score == 0 and player_score != 0:
        print("Computer wins")
    elif dealer_score != 0 and player_score == 0:
        print("You win")
    elif player_score >= 21 and dealer_score <= 21:
        print("You lost! The computer won!")
    elif dealer_score >= 21 and player_score <= 21:
        print("You won! The computer has lost!")
    elif player_score > dealer_score and player_score <= 21:
        print("You won!")
    else:
        print("Your lost!")


def play_game():
    print(logo)
    clear()
    user_cards = []
    computer_cards = []
    continue_game = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while continue_game:
        user_cards_total = calculate_score(user_cards)
        computer_cards_total = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}\n Your score: {user_cards_total}")
        print(f"Computer's cards: {computer_cards[0]}")

        if user_cards_total == 0 or computer_cards_total == 0 or user_cards_total > 21:
            continue_game = False
        else:
            user_deal = input(
                "Type 'hit' to draw another card or 'stay' to pass your turn: ").lower()
            if user_deal == "hit":
                user_cards.append(deal_card())
            else:
                continue_game = False

    while computer_cards_total != 0 and computer_cards_total < 17:
        computer_cards.append(deal_card())
        computer_cards_total = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}\n Your score: {user_cards_total}")
    print(
        f"Computer's cards: {computer_cards}\n Computer's score: {computer_cards_total}")
    print(compare(user_cards_total, computer_cards_total))


while input("Do you want to play a game? (y/n) ") == "y":
    clear()
    play_game()
else:
    clear()
    print("Bye!")
    exit()
