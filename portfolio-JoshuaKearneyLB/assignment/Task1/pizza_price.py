#!/usr/bin/env python3

"""
 - Every pizza is 12 pounds
 - 50% applied if tuesday is true (Not included in delivery costs -> must be done before delivery calculation)
 - Delivery is 2.50 extra if true
 - If the user is using app 25% discount is added
 - All validation must be done inside program
"""


def number_of_pizzas():
    valid_input = False
    pizza_amount_int = 0

    while not valid_input:
        pizza_amount = input("How many pizzas ordered? ")
        try:
            pizza_amount_int = int(pizza_amount)
            if pizza_amount_int < 1:
                print("Please enter a positive integer!")
            else:
                valid_input = True
        except ValueError:
            print("Please enter a number!")
    return pizza_amount_int


def tuesday_discount():
    valid_input = False
    tuesday = False

    while not valid_input:
        is_it_tuesday = input("Is it tuesday? ")
        if is_it_tuesday in ['y', 'Y']:
            tuesday = True
            valid_input = True
        elif is_it_tuesday in ['n', 'N']:
            tuesday = False
            valid_input = True
        else:
            print("Please answer \"N\" or \"N\".")
    return tuesday


def delivery_charge():
    valid_input = False
    delivery = False

    while not valid_input:
        delivery_required = input("Is delivery required? ")
        if delivery_required in ['y', 'Y']:
            delivery = True
            valid_input = True
        elif delivery_required in ['n', 'N']:
            delivery = False
            valid_input = True
        else:
            print("Please answer \"Y\" or \"N\".")
    return delivery


def using_app():
    valid_input = False
    app = False

    while not valid_input:
        app = input("Did the customer use the app? ")
        if app in ['y', 'Y']:
            app = True
            valid_input = True
        elif app in ['n', 'N']:
            app = False
            valid_input = True
        else:
            print("Please answer \"Y\" or \"N\".")
    return app


if __name__ == '__main__':
    print("BPP Price calculator")
    print("=====================")

    total_cost = 12 * (number_of_pizzas())
    if tuesday_discount():
        total_cost *= 0.75
    if using_app():
        total_cost *= 0.5
    if delivery_charge():
        total_cost += 2.50

    print("Final cost = £%.2f" % total_cost)
