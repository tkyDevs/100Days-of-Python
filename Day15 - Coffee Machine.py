def countMoney(coinStorageDict):
    """
    Returns the sum of all the coins in storage.
    """
    totalSum = 0
    for key in coinStorageDict:
        if key == "penny":
            totalSum += coinStorageDict[key]
        elif key == "nickel":
            totalSum += coinStorageDict[key] * 5
        elif key == "dime":
            totalSum += coinStorageDict[key] * 10
        elif key == "quarter":
            totalSum += coinStorageDict[key] * 25
        else:
            return "Invalid key found!"
    return totalSum


def makeCoinDict(quarter, dime, nickle, penny):
    """
    Return a dictionary of all coins.
    """
    return {
        "quarter": int(quarter),
        "dime": int(dime),
        "nickel": int(nickle),
        "penny": int(penny)
    }


def createReport():
    """
    Returns a fstring containing the remaining ingredients and total sum of money in coffee machine.
    """
    return (f"Water: {ingredientsStorage["water"]}ml\n"
            f"Milk: {ingredientsStorage["milk"]}ml\n"
            f"Coffee: {ingredientsStorage["coffee"]}g\n"
            f"Total Sum: ${PROFIT/100}\n")


def isEnoughIngredients(orderedBev):
    """
    Returns True if the coffee machine has enough ingredients for the order. Else, returns False.
    """
    if (ingredientsStorage["water"] < beverages[orderedBev][1] or
            ingredientsStorage["coffee"] < beverages[orderedBev][2] or
            ingredientsStorage["milk"] < beverages[orderedBev][3]):
        return False
    else:
        return True


def isEnoughMoney(orderedBev, payment):
    """
    Returns True if payment is enough for order. Else, returns False.
    """
    if beverages[orderedBev][0] <= payment:
        return True
    else:
        return False


def makeBeverage(orderedBev):
    """
    Subtracts ingredients used in the ordered beverage.
    """
    ingredientsStorage["water"] -= beverages[orderedBev][1]
    ingredientsStorage["coffee"] -= beverages[orderedBev][2]
    ingredientsStorage["milk"] -= beverages[orderedBev][3]


def refillIngredients():
    """
    Refills ingredients in the coffee machine.
    """
    ingredientsStorage["water"] = 1000
    ingredientsStorage["milk"] = 1000
    ingredientsStorage["coffee"] = 100
    print("Ingredients Refilled!")


beverages = {
    # beverageType: [price, water, coffee, milk]
    "espresso": [150, 50, 18, 0],
    "latte": [250, 200, 24, 150],
    "cappuccino": [350, 250, 24, 100]
}

ingredientsStorage = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

PROFIT = 0

isOver = False
while not isOver:
    order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if order == "report":
        print(createReport())
    elif order == "off":
        isOver = True
    else:
        print("Please insert coins.")
        quarters = input("How many quarters?: ").strip()
        dimes = input("How many dimes?: ").strip()
        nickles = input("How many nickles?: ").strip()
        pennies = input("How many pennies?: ").strip()
        customerMoney = countMoney(makeCoinDict(quarters, dimes, nickles, pennies))
        if isEnoughIngredients(order) and isEnoughMoney(order, customerMoney):
            print(f"Thank you very much! Your {order} is served.")
            PROFIT += beverages[order][0]
            makeBeverage(order)
            change = (customerMoney - beverages[order][0]) / 100
            print(f"Your change is ${change}.")
        elif not isEnoughMoney(order, customerMoney):
            print("Not enough credits for this beverage. money refunded.")
        else:
            print("Not enough ingredients. Money refunded. Please try again after refill.")
            refillIngredients()
