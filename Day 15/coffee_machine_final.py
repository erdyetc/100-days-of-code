def coffee_machine_1():
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
    
    on_status = "on"
    resources["money"] = 0

    while 1:
        if on_status == "on":
            x = coffee_machine_on(resources, on_status, MENU)
            if x == "off":
                on_status = "off"

        if on_status == "off":
            on_status = input("Do you want to turn the coffee machine back on? Type 'on' or 'off': ")

def coffee_machine_2():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 100,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 200,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 350,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 4.0,
        }
    }

    resources = {
        "water": 1000,
        "milk": 400,
        "coffee": 100,
    }
    
    on_status = "on"
    resources["money"] = 0

    while 1:
        if on_status == "on":
            x = coffee_machine_on(resources, on_status, MENU)
            if x == "off":
                on_status = "off"

        if on_status == "off":
            on_status = input("Do you want to turn the coffee machine back on? Type 'on' or 'off': ")

def coffee_machine_on(resources, on_status, MENU):
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    money_in_machine = resources["money"]

    #TODO1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    #TODO2: Turn off the Coffee Machine by entering “off” to the prompt.
    if user_order == "off":
        return "off"
    
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
        resources["water"] = water_left - water_needed
        resources["milk"] = milk_left - milk_needed
        resources["coffee"] = coffee_left - coffee_needed
        resources["money"] = money_in_machine + price
        if change > 0:
            print(f"Here is ${change:.2f} dollars in change")
        #TODO7: Make coffee
        print(f"Here is your {user_order}. Enjoy!")
        return
    else:
        print("Sorry, that's not enough money. Money refunded")
        return

machine_num = int(input("Which coffee machine would you like to use? 1 or 2: "))

if machine_num == 1:
    coffee_machine_1()
elif machine_num == 2:
    coffee_machine_2()