from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    order = input(f"What would you like? Choose from {options}: ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        final_order = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(final_order):
            if money_machine.make_payment(final_order.cost):
                coffee_maker.make_coffee(final_order)