from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_on = True
while machine_on:
    # Get the available menu items
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:  # Find the drink in the menu
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
