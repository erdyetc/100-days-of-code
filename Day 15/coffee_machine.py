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

def how_much_water():
    return resources["water"]

def how_much_milk():
    return resources["milk"]

def how_much_coffee():
    return resources["coffee"]

resources["money"] = 0

def how_much_money():
    return resources["money"]

resources["status"] = "turn on"

def what_status():
    return resources["status"]

def coffee_machine_on():
    #TODO1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #TODO2: Turn off the Coffee Machine by entering “off” to the prompt.
    if user_order == "off":
        status = "turn off"
        return [water_left, milk_left, coffee_left, money_in_machine, status]

    #TODO3: Print report when the user enters “report” to the prompt
    water_left = how_much_water()
    milk_left = how_much_milk()
    coffee_left = how_much_coffee()
    money_in_machine = how_much_money()
    status = what_status()
    
    if user_order == "report":
        print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${money_in_machine}")
        print(water_left,milk_left, coffee_left, money_in_machine, status)
        return [water_left, milk_left, coffee_left, money_in_machine, status]

    #TODO4: Check resources sufficient when the user chooses a drink
    water_needed = MENU[user_order]["ingredients"].get("water",0)
    milk_needed = MENU[user_order]["ingredients"].get("milk",0)
    coffee_needed = MENU[user_order]["ingredients"].get("coffee",0)

    if water_needed > water_left:
        print("Sorry, not enough water in machine.")
        return [water_left, milk_left, coffee_left, money_in_machine, status]
    if milk_needed > milk_left:
        print("Sorry, not enough milk in machine.")
        return [water_left, milk_left, coffee_left, money_in_machine, status]
    if coffee_needed > coffee_left:
        print("Sorry, not enough coffee in machine.")
        return [water_left, milk_left, coffee_left, money_in_machine, status]

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
        return [water_left, milk_left, coffee_left, money_in_machine, status]
    else:
        print("Sorry, that's not enough money. Money refunded")
        return [water_left, milk_left, coffee_left, money_in_machine, status]

on_status = resources["status"]
while not on_status == "turn off":
    new_resources = coffee_machine_on()
    resources["water"] = new_resources[0]
    resources["milk"] = new_resources[1]
    resources["coffee"] = new_resources[2]   
    resources["money"] = new_resources[3]
    resources["status"] = new_resources[4]