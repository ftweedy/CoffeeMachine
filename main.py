# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

menu = {
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


profit = 0


def check_water(selection):
    return resources["water"] >= menu[selection]["ingredients"]["water"]


def check_milk(selection):
    return resources["milk"] >= menu[selection]["ingredients"]["milk"]


def check_coffee(selection):
    return resources["coffee"] >= menu[selection]["ingredients"]["coffee"]


def print_report():
    global resources
    global profit
    for resource in resources:
        print(resource + " " + str(resources[resource]))
    print(profit)


def make_drink(selection):
    global resources
    resources["water"] -= menu[selection]["ingredients"]["water"]
    resources["milk"] -= menu[selection]["ingredients"]["milk"]
    resources["coffee"] -= menu[selection]["ingredients"]["coffee"]
    print("Your coffee is ready, enjoy!")


def check_coins(selection):
    global profit
    pennies = input("Input number of pennies: ")
    nickels = input("Input number of nickels: ")
    dimes = input("Input number of dimes: ")
    quarters = input("Input number of quarters: ")
    total_money = (.01*float(pennies)) + (.05*float(nickels)) + (.1*float(dimes)) + (.25*float(quarters))
    if menu[selection]["cost"] > total_money:
        print("Sorry, that's not enough money.  Money Refunded.")
        return
    else:
        profit = profit + menu[selection]["cost"]
        print(f"Here's your change: {total_money-menu[selection]['cost']}")
        make_drink(selection)



def check_resources(selection):
    if not check_water(selection):
        print("Sorry there is not enough water.")
    if not check_milk(selection):
        print("sorry there is not enough milk.")
    if not check_coffee(selection):
        print("Sorry there is not enough water.")
    elif check_water(selection) & check_milk(selection) & check_coffee(selection):
        check_coins(selection)


def main():
    # Use a breakpoint in the code line below to debug your script.
    more_commands = True
    while more_commands:
        selection = input('What would you like? (espresso/latte/cappuccino:')
        if selection == 'off':
            exit()
        elif selection == 'report':
            print_report()
        elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
            check_resources(selection)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
