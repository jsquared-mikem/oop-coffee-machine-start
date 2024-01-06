from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

the_menu = Menu()
money_machine = MoneyMachine()
jeans_maker = CoffeeMaker()

is_on = True

while is_on:
    option = the_menu.get_items()
    choice = input(f"What would you like? {option}): ")

    if choice.lower() == "off":
        is_on = False

    elif choice.lower() == "report":
        jeans_maker.report()
        money_machine.report()

    else:
        drink = the_menu.find_drink(choice)
        available = jeans_maker.is_resource_sufficient(drink)

        if available:
            money_machine.make_payment(drink.cost)
            jeans_maker.make_coffee(drink)

