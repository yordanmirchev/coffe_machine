from data import *
from art import logo

""" Avaiable options, repot/off and recharge are hidden"""
OPTIONS = ["espresso", "latte", "cappuccino", "report", "off", "recharge"]

profit = 0


def prompt_for_action():
    """ Ask the user for input"""
    choice = ""
    while choice not in OPTIONS:
        choice = input("What would you like? (espresso/latte/cappuccino):")

    return choice


def recharge():
    """ Refill resources with 1000 each"""
    global resources
    resources = {"water": 1000,
                 "milk": 1000,
                 "coffee": 1000,
                 }
    print("Refilling")
    print_report()


def print_report():
    """ Print current status reoprt"""
    print(
        f"Current status report:\n\tWater: {resources['water']} ml\n\tMilk: {resources['milk']} ml\n\tCoffee: {resources['coffee']}g\n\tProfit: ${profit}")


def has_sufficient_resource(present, required):
    if present < required:
        return False
    return True


def refund(sum):
    print(f"Please take your coins: ${sum}")


def process_payment(cost):
    """ Asks user for coins, sum them and evaluate if enough for the drink"""
    money = process_coins();
    if money < cost:
        print(f"Sorry there is not enough money, required: ${cost}, provided: ${money}.")
        refund(money)
        return False
    else:
        print("Enough resources.")
        change = round(money - cost, 2);
        if change >= 0:
            if change > 0:
                refund(round(change, 2))
            return True


def has_enough_resources(item):
    """ Checks if enough resources available for item"""
    drink = MENU[item]
    ingredients = drink["ingredients"]

    print(f"Selected {item}, it requites: ")
    for ingredient in ingredients:
        print(f"{ingredient} : {ingredients[ingredient]}")

    for resource in ingredients:
        global resources
        present = resources[resource]
        required = ingredients[resource]
        if not has_sufficient_resource(present, required):
            print(f"Not enough {resource}")
            return False

        return True


def get_coins(type):
    """Asks user to provide coins count and evaluates if positive integer provided"""
    coin = -1
    while True:
        user_input = input(f"{type} count: ")
        try:
            coin = int(user_input)
            if coin >= 0:
                break
        except ValueError:
            pass

    return coin


def process_coins():
    """ Calculates the coins total"""
    quarters = get_coins("quarters")
    dimes = get_coins("dimes")
    nickles = get_coins("nickles")
    pennies = get_coins("pennies")

    total = 0
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickles * 0.05
    total += pennies * 0.01

    print(f"Total inserted: ${total}")

    return total


def make_coffee(selection):
    """Prepare the drink deduct resources and add profit"""

    for resource in MENU[selection]["ingredients"]:
        global resources
        resources[resource] -= MENU[selection]["ingredients"][resource]
    global profit
    profit += MENU[selection]["cost"]

    print(f"Here is your {selection}. Enjoy!")


def run_machine():
    """ main method to run the machine"""
    print(logo)
    stop = False

    while not stop:
        selection = prompt_for_action()
        if selection == 'report':
            print_report()
        if selection == 'off':
            stop = True
            print("Turning off.")
        if selection == 'recharge':
            recharge()
        if selection in ["espresso", "latte", "cappuccino"]:
            if has_enough_resources(selection):
                if process_payment(MENU[selection]["cost"]):
                    print_report()
                    make_coffee(selection)
                    print_report()


run_machine()
