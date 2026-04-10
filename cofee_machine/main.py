import art
import constants
import resources
def take_input():
    """Takes user input"""
    user_input=input("What would you like to have expresso/latte/cappuccino/report? ").strip().lower()
    return user_input

def validate_input(user_input):
    """Validates user input"""
    if user_input in constants.INPUTS:
        return True
    else:
        return False
def print_report():
    """Prints report on coffee machine"""
    print(f"Water: {resources.RESOURCES['water']}ml")
    print(f"Milk: {resources.RESOURCES['milk']}ml")
    print(f"Coffee: {resources.RESOURCES['coffee']}g")

def take_coins():
    """Takes and processes monetary coins"""
    try:
        quarters =input("How many quarters?:")
        dimes=input("How many dimes?:")
        nickel=input("How many nickel?:")
        pennies=input("How many pennies?:")
        total= int(quarters)*constants.COINS["quarters"] + int(dimes)*constants.COINS["dimes"] + int(nickel)*constants.COINS["nickles"] + int(pennies)*constants.COINS["pennies"]
        return total
    except ValueError:
        print("Please enter a valid number of coins")
        return take_coins()
def check_resources(user_input):
    """Checks if enough resources are available"""
    if user_input == "espresso" and constants.MENU["espresso"]["ingredients"]["water"]<=resources.RESOURCES["water"] and constants.MENU["espresso"]["ingredients"]["coffee"]<=resources.RESOURCES["coffee"]:
        return True
    elif user_input == "latte" and constants.MENU["latte"]["ingredients"]["water"]<=resources.RESOURCES["water"] and constants.MENU["latte"]["ingredients"]["coffee"]<=resources.RESOURCES["coffee"] and constants.MENU["latte"]["ingredients"]["milk"]<=resources.RESOURCES["milk"]:
        return True
    elif user_input == "cappuccino" and constants.MENU["cappuccino"]["ingredients"]["water"]<=resources.RESOURCES["water"] and constants.MENU["cappuccino"]["ingredients"]["coffee"]<=resources.RESOURCES["coffee"] and constants.MENU["cappuccino"]["ingredients"]["milk"]<=resources.RESOURCES["milk"]:
        return True
    else:
        return False

def make_transaction(user_input,total_amount):
    """Make transaction against coffee choice"""
    if total_amount >= constants.MENU[user_input]["cost"]:
        change= total_amount - constants.MENU[user_input]["cost"]
        print(f"Here is ${change} in change")
        print(f"Here is your {user_input} ☕️. Enjoy!")
        resources.RESOURCES["water"] -= constants.MENU[user_input]["ingredients"]["water"]
        resources.RESOURCES["coffee"] -= constants.MENU[user_input]["ingredients"]["coffee"]
        if user_input != "espresso":
            resources.RESOURCES["milk"] -= constants.MENU[user_input]["ingredients"]["milk"]
        print("Updated report: ")
        print_report()
        main()
    else:
        print("Sorry that's not enough money. Money refunded.")
        main()


def process_request(user_input):
    """Process user input"""
    if user_input == "report":
        print_report()
        main()
    else :
        if check_resources(user_input):
            print("Insert coin")
            total_amount=take_coins()
            make_transaction(user_input,total_amount)
        else:
            print("Sorry there is not enough resources")
            refill_resources=input("Want to fill the resources again?").strip().lower()
            if refill_resources == "y":
                resources.refill_resources()
                main()
            else:
                main()




def main():
    """Driving method for coffee machine"""
    user_input = take_input()
    if validate_input(user_input):
        process_request(user_input)
    else:
        take_input()

print(art.logo)
main()