from coffe_resource import resources, MENU


def rescource(res):
    res_watter = res["water"]
    res_milk = res["milk"]
    res_coffee = res["coffee"]
    return f"Water: {res_watter}ml\n" \
           f"Milk: {res_milk}ml\n" \
           f"Coffee: {res_coffee}g"


total = 0
money = 0


def if_enough(total1):
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total1 = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if total1 >= MENU[my_wish]['cost']:
        print(f"Here is ${total1 - MENU[my_wish]['cost']:.2f} in change.")
        print(f"Here is your {my_wish} enjoy!")
        money += MENU[my_wish]['cost']
        if my_wish == 'latte' or my_wish == 'cappuccino':
            resources["water"] -= MENU[my_wish]["ingredients"]["water"]
            resources["milk"] -= MENU[my_wish]["ingredients"]["milk"]
            resources["coffee"] -= MENU[my_wish]["ingredients"]["coffee"]
        elif my_wish == 'espresso':
            resources["water"] -= MENU[my_wish]["ingredients"]["water"]
            resources["coffee"] -= MENU[my_wish]["ingredients"]["coffee"]
    else:
        print("Sorry not enough money. Money refunded.")


while True:
    my_wish = input("What would you like? (espresso/latte/cappuccino): ")
    if my_wish == "report":
        print(rescource(resources))
        print(f"Money: ${money}")
    if my_wish == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            if_enough(total)
            continue
        elif resources["water"] <= 200:
            print("There is not enough water.")
            continue
        elif resources["milk"] <= 150:
            print("There is not enough milk.")
            continue
        elif resources["water"] <= 24:
            print("There is not enough coffee.")
            continue
    if my_wish == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            if_enough(total)
            continue
        elif resources["water"] <= 250:
            print("There is not enough water.")
            continue
        elif resources["milk"] <= 100:
            print("There is not enough milk.")
            continue
        elif resources["water"] <= 24:
            print("There is not enough coffee.")
            continue
    if my_wish == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            if_enough(total)
            continue
        elif resources["water"] <= 50:
            print("There is not enough water.")
            continue
        elif resources["water"] <= 18:
            print("There is not enough coffee.")
            continue
    if my_wish == 'off':
        break
