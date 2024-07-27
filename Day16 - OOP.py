# Procedural Programming: The code runs from top to bottom in the same file.
#   It can get very confusing since the number of relations in the code tend to increase and become more complex.

# Object-Oriented Programming: The code is separated into specific classes.
#   Similar to a restaurant where there is a server/waiter/cook/manager. Classes separate in properties and methods.
#   Additionally, we can create different objects of the same class.

from turtle import Turtle, Screen

import Day16_coffee_maker
import Day16_menu
import Day16_money_machine

# How to create an instance of a class:
# nameOfInstance = class()
#instance = Turtle()

# Attributes: Characteristics of the instance. Example: speed is an attribute of a car.
# Methods: Functions linked to a class is a method. Everything that the class can DO. Example: A car can move and stop.

# How to install python packages
# In the terminal: pip install packageName

# How to call a method from a class: instanceName.methodName()
#instance.shape("turtle")
#instance.color("cyan3")

# myScreen = Screen()
# myScreen.exitonclick()

# Day16 Project:
coffee_maker = Day16_coffee_maker.CoffeeMaker()
menu = Day16_menu.Menu()
money_machine = Day16_money_machine.MoneyMachine()

isOver = False
while not isOver:
    allItems = menu.get_items()
    order = input(f"What would you like? {allItems}: ").strip().lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        isOver = True
    else:
        beverageOrdered = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(beverageOrdered):
            customerMoney = money_machine.make_payment(beverageOrdered.cost)
            coffee_maker.make_coffee(beverageOrdered)

