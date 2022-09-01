import os
import time
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def clear(seconds: int):
    """This function clears the screen after a given amount of time"""
    time.sleep(seconds)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


money_machine = MoneyMachine()  # Create a MoneyMachine object
coffee_maker = CoffeeMaker()    # Create a CoffeeMaker object
menu = Menu()                # Create a Menu object
menu_item = MenuItem        # Create a MenuItem object


continue_running = True
while continue_running:     # Main loop
    instruction = int(
        input("What would you like to do?\n1. Make a coffee\n2. Report\n3. Exit\n"))
    if instruction == 1:
        options = menu.get_items()  # Get the available menu items
        # Get the user's order
        user_order = input(f"What would you like to order?\n{options}\n")
        # Find the order in the menu
        order = menu.find_drink(user_order)
        resource = coffee_maker.is_resource_sufficient(
            order)      # Check if the resources are sufficient
        payment = money_machine.make_payment(
            order.cost)        # Receive the payment
        if resource and payment:        # If the resources are sufficient and the payment is accepted, make the coffee
            coffee_maker.make_coffee(order)
        clear(3)
    elif instruction == 2:
        print(money_machine.report())       # Print the money machine report
        print(coffee_maker.report())        # Print the coffee maker report
        clear(3)
    elif instruction == 3:
        continue_running = False
    else:
        print("Invalid input!")
        clear(3)
