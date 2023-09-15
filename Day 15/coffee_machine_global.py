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

water_left = resources["water"]
milk_left = resources["milk"]
coffee_left = resources["coffee"]
resources["money"] = 0
money_in_machine = resources["money"]
on_status = "on"

def coffee_machine_on():
    global water_left
    global milk_left
    global coffee_left
    global money_in_machine
    global on_status

    #TODO1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #TODO2: Turn off the Coffee Machine by entering “off” to the prompt.
    if user_order == "off":
        on_status = "off"
        return
    
    #TODO3: Print report when the user enters “report” to the prompt
    if user_order == "report":
        print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${money_in_machine}")
        return

    #TODO4: Check resources sufficient when the user chooses a drink
    water_needed = MENU[user_order]["ingredients"].get("water",0)
    milk_needed = MENU[user_order]["ingredients"].get("milk",0)
    coffee_needed = MENU[user_order]["ingredients"].get("coffee",0)

    if water_needed > water_left:
        print("Sorry, not enough water in machine.")
        return
    if milk_needed > milk_left:
        print("Sorry, not enough milk in machine.")
        return
    if coffee_needed > coffee_left:
        print("Sorry, not enough coffee in machine.")
        return

    #TODO5: Process coins: If there are sufficient resources, prompt the user to insert coins and calculate value
    price = MENU[user_order].get("cost","N/A")

    print(f"The price of a/an {user_order} is ${price}. Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    contribution = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    #TODO6: Check if transaction successful
    if contribution >= price:
        change = float(contribution - price)
        water_left -= water_needed
        milk_left -= milk_needed
        coffee_left -= coffee_needed
        money_in_machine += price
        if change > 0:
            print(f"Here is ${change:.2f} dollars in change")
        #TODO7: Make coffee
        print(f"Here is your {user_order}. Enjoy!")
        return
    else:
        print("Sorry, that's not enough money. Money refunded")
        return
    
while 1:
    if on_status == "on":
        coffee_machine_on()

    if on_status == "off":
        on_status = input("Do you want to turn the coffee machine back on? Type 'on' or 'off': ")