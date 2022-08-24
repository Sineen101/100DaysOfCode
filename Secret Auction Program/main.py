import os

logo = '''
                    _   _             
    /\             | | (_)            
   /  \  _   _  ___| |_ _  ___  _ __  
  / /\ \| | | |/ __| __| |/ _ \| '_ \ 
 / ____ \ |_| | (__| |_| | (_) | | | |
/_/    \_\__,_|\___|\__|_|\___/|_| |_|
    
    
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    # clear screen


bids = {}


def find_highest_bid(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        bid = bidding[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    return winner, highest_bid


bidding_end = False
while not bidding_end:
    name = input("What is your name?\n ")
    price = int(input("What is the price of the item?\n $"))
    bids[name] = price
    bidding_continue = input("Are there any more bids? Yes/No\n ").lower()
    if bidding_continue == "no":
        bidding_end = True
        find_highest_bid(bids)
    elif bidding_continue == "yes":
        clear()
# find highest bid and print winner
print(
    f"The winner is {find_highest_bid(bids)[0]} with a bid of ${find_highest_bid(bids)[1]}")
