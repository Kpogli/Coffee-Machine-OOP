from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects creations
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Make the machine run while on
machine_running = True

while machine_running:
    # Prompt user
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        machine_running = False
    # Print report by entering “report” to the prompt.
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        # Get drink object by using find drink method
        drink = menu.find_drink(user_input)
        # Check if there are enough resources to make the drink
        if coffee_maker.is_resource_sufficient(drink):
            # Make_Payment method already includes the process coins functionality before making payment
            if money_machine.make_payment(drink.cost):
                # Make the coffee if the make_payment methods results truthy
                coffee_maker.make_coffee(drink)
    else:
        print("Invalid selection")


