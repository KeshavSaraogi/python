
def displayOptions():
    decision = int(input(("1. Print Report\n2. Order Coffee\n3. Exit\nPress Your Option: ")))
    if decision == 1:
        return 1
    elif decision == 2:
        return 2
    elif decision == 3:
        return 3
    else:
        return -1


def selectACoffee():
    print("Your Options For Coffee Are As Follows: ")
    coffee = int(input("1. Espresso\n2. Latte\n3. Cappuccino\nPress Your Option: "))

    if coffee == 1:
        checkForCoins(1)
        return 1
    elif coffee == 2:
        checkForCoins(2)
        return 2
    elif coffee == 3:
        checkForCoins(3)
        return 3
    else:
        return -1

def checkForCoins(num):
    changeMoney = 0
    if num == 1:
        print(f"An Espresso Costs for ${priceForCoffee(1)}")
        totalMoney = processCoins()
        if totalMoney >= priceForCoffee(1):
            changeMoney = totalMoney - priceForCoffee(1)
            print("Processing Your Espresso!")
            print(f"Your Change Amount Is: ${changeMoney}")
        else:
            print("Not Enough Funds.")
            print("Money Refunded.")
    
    elif num == 2:
        print(f"A Latte Costs for ${priceForCoffee(2)}")
        totalMoney = processCoins()
        if totalMoney >= priceForCoffee(2):
            changeMoney = totalMoney - priceForCoffee(2)
            print("Processing Your Latte!")
            print(f"Your Change Amount Is: ${changeMoney}")
        else:
            print("Not Enough Funds.")
            print("Money Refunded.")
    
    elif num == 3: 
        print(f"A Cappuccino Costs for ${priceForCoffee(3)}")
        totalMoney = processCoins()
        if totalMoney >= priceForCoffee(3):
            changeMoney = totalMoney - priceForCoffee(3)
            print("Processing Your Cappucino!")
            print(f"Your Change Amount Is: ${changeMoney}")
        else:
            print("Not Enough Funds.")
            print("Money Refunded.")

def processCoins():
    totalMoneyDeposited = 0

    print("Enter Coins To Process Order: ")
    penny = int(input("1. Pennies: "))
    nickel = int(input("2. Nickels: "))
    dime = int(input("3. Dimes: "))
    quarter = int(input("4. Quarters: "))

    totalMoneyDeposited = (penny * 0.01) + (nickel * 0.05) + (dime * 0.1) + (quarter * 0.25)

    print(f"You Deposited: ${totalMoneyDeposited}")
    return totalMoneyDeposited 

def checkForIngridients(num):
    water = 300
    milk = 200
    coffee = 100

    if num == 1:
        requiredWater = 50
        requiredCoffee = 18
        requiredMilk = 0
        if water > requiredWater and coffee > requiredCoffee and milk > requiredMilk:
            water = water - requiredWater
            coffee = coffee - requiredCoffee
            milk = milk - requiredMilk
            return [milk, coffee, water]
        else:
            return -1
    
    if num == 2:
        requiredWater = 200
        requiredCoffee = 150
        requiredMilk = 24
        if water > requiredWater and coffee > requiredCoffee and milk > requiredMilk:
            water = water - requiredWater
            coffee = coffee - requiredCoffee
            milk = milk - requiredMilk
            return [milk, coffee, water]
        else:
            return -1
    
    if num == 3:
        requiredWater = 250
        requiredCoffee = 100
        requiredMilk = 24
        if water > requiredWater and coffee > requiredCoffee and milk > requiredMilk:
            water = water - requiredWater
            coffee = coffee - requiredCoffee
            milk = milk - requiredMilk
            return [milk, coffee, water]
        else:
            return -1

def priceForCoffee(coffee):
    if coffee == 1:
        return 1.50
    elif coffee == 2:
        return 2.50
    else:
        return 3.00

def reportForMachine(milk, coffee, water):
    return milk, coffee, water

def main():
    water = 300
    milk = 200
    coffee = 100
    exitTheMachine = False

    while exitTheMachine is False:
        print("Welcome To The Coffee Shop")
        decision = displayOptions()
        if decision == 1:
            milk, coffee, water = reportForMachine(milk, coffee, water)
            print(f"Milk: {milk}ml\nCoffee: {coffee}ml\nWater: {water}ml")
        if decision == 2:
            coffee = selectACoffee()
            milk, coffee, water = checkForIngridients(coffee)
            print(milk, coffee, water)
            displayOptions()
        if decision == 3:
            break

if __name__ == "__main__":
    main()
