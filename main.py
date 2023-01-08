from data import MENU
from data import resources
from art import logo

# TODO : Add logo

OPTIONS = ["espresso", "latte", "cappuccino", "report", "off", "recharge"]

proffit = 0


def prompt_for_action():
    choice = ""
    while choice not in OPTIONS:
        choice = input("What would you like? (espresso/latte/cappuccino):")

    return choice


# TODO : fix recharge
def recharge():
    var = {}

    var = {"water": 1000,
           "milk": 1000,
           "coffee": 1000,
           }

    return var


def print_report(resources, proffit):
    print(
        f"Current status report:\n\tWater: {resources['water']} ml\n\tMilk: {resources['milk']} ml\n\tCoffee: {resources['coffee']}g\n\tProffit: ${proffit}")


def has_sufficient_resource(present, required):
    if present < required:
        return False
    return True


def refund(sum):
    print(f"Please take your coins: ${sum}")


def process_payment(cost):
    """ Provides money refund  if insufficient, provides change if more and returns 0 if sufficient"""
    money = process_coins();
    if money < cost:
        print(f"Sorry there is not enough money, required: ${cost}, provided: ${money}.")
        refund(money)
        return -1;
    else:
        print("Enough resources.")
        change = round(money - cost, 2);
        if change >= 0:
            if change > 0:
                refund(round(change, 2))
            return 0


def check_resources(item):
    drink = MENU[item]
    ingredients = drink["ingredients"]
    price = drink["cost"]

    print(f"Selected {item}, it requites: ")
    for ingredient in ingredients:
        print(f"{ingredient} : {ingredients[ingredient]}")


    for resource in ingredients:
        present = resources[resource]
        required = ingredients[resource]
        if not has_sufficient_resource(present, required):
            print(f"Not enough {resource}")
            return -1

        return process_payment(price)


# TODO : fix check
def get_coins(type):
    coin = ""
    while not isinstance(coin, int):
        coin = int(input(f"{type} count: "))
        print(f"Inserted {coin} {type}")
        return coin


def process_coins():
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


def add_profit(sum):
    print(f"add_profit: {sum}")


def make_coffee(selection):
    used_resources = {}

    for resource in MENU[selection]["ingredients"]:
        used_resources[resource] = MENU[selection]["ingredients"][resource]

    current_status = {"proffit": MENU[selection]["cost"],
                      "resources": used_resources}

    print(f"Here is your {selection}. Enjoy!")
    return current_status




def run():
    print(logo)
    stop = False
    current_proffit = proffit;
    current_resources = resources;

    while not stop:
        selection = prompt_for_action()

        if selection == 'report':
            print_report(current_resources, current_proffit)
        if selection == 'off':
            stop = True
            print("Turning off.")
        if selection == 'recharge':
            recharge()
        if selection in ["espresso", "latte", "cappuccino"]:
            if check_resources(selection) == 0:
                print_report(current_resources, current_proffit)
                update = make_coffee(selection)
                current_proffit += update["proffit"]
                current_resources_diff = update["resources"]
                for resource in current_resources_diff:
                    current_resources[resource] -= current_resources_diff[resource]

                print_report(current_resources, current_proffit)


# test()
run()
