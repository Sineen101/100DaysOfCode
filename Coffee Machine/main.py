MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def menu():
    """This function prints the menu and takes the order from the user"""
    order = input(
        "What do you want to buy? <Type out your drink's name>\n1. Espresso\n2. Latte\n3. Cappuccino\n").lower()
    if order == "espresso":
        order = MENU[order]
        order_cost = order["cost"]
        print(f'That will be ${order_cost}')
        return order, order_cost
    elif order == "latte":
        order = MENU["latte"]
        order_cost = order["cost"]
        print(f'That will be ${order_cost}')
        return order, order_cost
    elif order == "cappuccino":
        order = MENU["cappuccino"]
        order_cost = order["cost"]
        print(f'That will be ${order_cost}')
        return order, order_cost
    else:
        print("Invalid selection")
        exit()


def payment(order_cost):
    """This function recieves and calculates the payment"""
    print("Please insert coins!")
    Quarters = int(input("Quarters: ")) * 0.25
    Dimes = int(input("Dimes: ")) * 0.10
    Nickles = int(input("Nickles: ")) * 0.05
    Pennies = int(input("Pennies: ")) * 0.01
    total_payment = Quarters + Dimes + Nickles + Pennies
    if total_payment >= order_cost:
        global profit
        profit += order_cost
        change = total_payment - order_cost
        print(
            f'Your change is ${round(change,2)}.\nWait...Your drink is being prepared.\nEnjoy your coffee!')
    elif total_payment < order_cost:
        print("Sorry that's not enough money.\nMoney refunded!")
    elif total_payment == order_cost:
        return True


def resources_check(order):
    """This function checks if the resources are enough to make the order"""
    order_ingredients = order["ingredients"]
    if order == MENU["espresso"]:
        if resources["water"] >= order_ingredients["water"] and resources["coffee"] >= order_ingredients["coffee"]:
            resources["water"] -= order_ingredients["water"]
            resources["coffee"] -= order_ingredients["coffee"]
            return True
        else:
            print("Sorry, not enough resources to make the order! Money refunded!")
            return False
    elif order == MENU["latte"] or order == MENU["cappuccino"]:
        if resources["water"] >= order_ingredients["water"] and resources["coffee"] >= order_ingredients["coffee"] and resources["milk"] >= order_ingredients["milk"]:
            resources["water"] -= order_ingredients["water"]
            resources["coffee"] -= order_ingredients["coffee"]
            resources["milk"] -= order_ingredients["milk"]
            return True
        else:
            print("Sorry, not enough resources to make the order! Money refunded!")
            return False
    else:
        return False


profit = 0
run_machine = True
while run_machine:
    instruction = int(input(
        "What would you like to do? Enter the number of choice:\n1. Make an order\n2. Print report\n3. Off\n"))
    if instruction == 1:
        user_order = menu()
        payment(user_order[1])
        resources_check(user_order[0])
    elif instruction == 2:
        print(f"Remaining resources: {resources}\nProfit: ${profit}")
    elif instruction == 3:
        run_machine = False
    else:
        print("Wrong input")
