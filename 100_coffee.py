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
    "money": 0
}

coins = {
    "quarters": .25,
    "dimes": .10,
    "nickles": .05,
    "pennies": .01
}


def supply_report():
    """prints the current supplies"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    if resources["money"] > 0:
        print(f"Money: ${resources["money"]}")


def resource_stocked(drinkie):
    """Compares the needed ingredients to the available ones, returning true if all ingredients are available"""
    water_needed = MENU.get(drinkie).get("ingredients").get("water", 0)
    milk_needed = MENU.get(drinkie).get("ingredients").get("milk", 0)
    coffee_needed = MENU.get(drinkie).get("ingredients").get("coffee", 0)

    if water_needed > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif milk_needed > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif coffee_needed > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def payment_processing():
    """asks the user for payment and returns the total value of all coins paid"""
    print("Please insert coins.")
    num_quarters = float(input("How many quarters?: "))
    num_dimes = float(input("How many dimes?: "))
    num_nickles = float(input("How many nickles?: "))
    num_pennies = float(input("How many pennies?: "))

    paid = float(
        (num_quarters*coins["quarters"]) +
        (num_dimes*coins["dimes"]) +
        (num_nickles*coins["nickles"]) +
        (num_pennies*coins["pennies"])
    )

    return paid


vend = True

while vend:
    # Todo: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    #    a. Check the user’s input to decide what to do next.
    #    b. The prompt should show every time action has completed, e.g. once the drink is
    #    dispensed. The prompt should show again to serve the next customer.

    order = input(f"What would you like? (espresso/latte/cappuccino): ")

    # Todo: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    #    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    #    the machine. Your code should end execution when this happens.

    if order == "off":
        print("🫡 Entering maintenance mode and powering off, goodbye :) 🫡")
        break

    # Todo: 3. Print report.
    #    a. When the user enters “report” to the prompt, a report should be generated that shows
    #    the current resource values. e.g.
    #    Water: 100ml
    #    Milk: 50ml
    #    Coffee: 76g
    #    Money: $2.5

    elif order == "report":
        supply_report()

    # Todo:  4. Check resources sufficient?
    #    a. When the user chooses a drink, the program should check if there are enough
    #    resources to make that drink.
    #    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    #    not continue to make the drink but print: “Sorry there is not enough water.”
    #    c. The same should happen if another resource is depleted, e.g. milk or coffee.

    elif order == "espresso" or "latte" or "cappuccino":
        if resource_stocked(order):

            # Todo:  5. Process coins.
            #    a. If there are sufficient resources to make the drink selected, then the program should
            #    prompt the user to insert coins.
            #    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            #    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
            #    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

            payment = payment_processing()

            # Todo:  6. Check transaction successful?
            #    a. Check that the user has inserted enough money to purchase the drink they selected.
            #    E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
            #    program should say “Sorry that's not enough money. Money refunded.”.
            #    b. But if the user has inserted enough money, then the cost of the drink gets added to the
            #    machine as the profit and this will be reflected the next time “report” is triggered. E.g.
            #    Water: 100ml
            #    Milk: 50ml
            #    Coffee: 76g
            #    Money: $2.5
            #    c. If the user has inserted too much money, the machine should offer change.
            #    E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
            #    places.

            if payment >= MENU[order]["cost"]:
                resources["money"] += MENU[order]["cost"]
                if payment > MENU[order]["cost"]:
                    refund = round(payment - MENU[order]["cost"], 2)
                    print(f"Here is ${refund} dollars in change.")

                # Todo:  7. Make Coffee.
                #    a. If the transaction is successful and there are enough resources to make the drink the
                #    user selected, then the ingredients to make the drink should be deducted from the
                #    coffee machine resources.
                #    E.g. report before purchasing latte:
                #    Water: 300ml
                #    Milk: 200ml
                #    Coffee: 100g
                #    Money: $0
                #    Report after purchasing latte:
                #    Water: 100ml
                #    Milk: 50ml
                #    Coffee: 76g
                #    Money: $2.5
                #    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
                #    latte was their choice of drink.

                resources["water"] -= MENU[order]["ingredients"].get("water", 0)
                resources["milk"] -= MENU[order]["ingredients"].get("milk", 0)
                resources["coffee"] -= MENU[order]["ingredients"].get("coffee", 0)

                supply_report()

                print(f"☕ Here is your {order}. Enjoy! ☕")

            else:
                print("Sorry that's not enough money. Money refunded.")
