import os
import time
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def clear(seconds: int):
    time.sleep(seconds)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_item = MenuItem


continue_running = True
while continue_running:
    instruction = int(
        input("What would you like to do?\n1. Make a coffee\n2. Report\n3. Exit\n"))
    if instruction == 1:
        options = menu.get_items()
        user_order = input(f"What would you like to order?\n{options}\n")
        order = menu.find_drink(user_order)
        resource = coffee_maker.is_resource_sufficient(order)
        payment = money_machine.make_payment(order.cost)
        if resource and payment:
            coffee_maker.make_coffee(order)
        clear(3)
    elif instruction == 2:
        print(money_machine.report())
        print(coffee_maker.report())
        clear(3)
    elif instruction == 3:
        continue_running = False
    else:
        print("Invalid input!")
        clear(3)
