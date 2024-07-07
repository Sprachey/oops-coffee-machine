from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeemachine=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

is_on=True
while is_on:
    choice=input("Enter name of the drink: ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffeemachine.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffeemachine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemachine.make_coffee(drink)



