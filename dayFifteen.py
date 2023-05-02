water = 300
milk = 200
coffee = 100

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
        checkForFunds(1)
        return 1
    elif coffee == 2:
        checkForFunds(2)
        return 2
    elif coffee == 3:
        checkForFunds(3)
        return 3
    else:
        return -1

def checkForFunds(num):
    changeMoney = 0
    if num == 1:
        print(f"An Espresso Costs for ${priceForCoffee(1)}")
        totalMoney = processCoins()
        if totalMoney >= priceForCoffee(1):
            changeMoney = totalMoney - priceForCoffee(1)
            print("Processing Your Coffee!")
            print(f"Your Change Amount Is: ${changeMoney}")
    
    elif num == 2:
        print(f"A Latte Costs for ${priceForCoffee(2)}")
        totalMoney = processCoins()
        if totalMoney >= priceForCoffee(2):
            changeMoney = totalMoney - priceForCoffee(2)
            print("Processing Your Coffee!")
            print(f"Your Change Amount Is: ${changeMoney}")
    
    elif num == 3: 
        print(f"A Cappuccino Costs for ${priceForCoffee(3)}")
        totalMoney = processCoins()
        if totalMoney >= priceForCoffee(3):
            changeMoney = totalMoney - priceForCoffee(3)
            print("Processing Your Coffee!")
            print(f"Your Change Amount Is: ${changeMoney}")

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


def priceForCoffee(coffee):
    if coffee == 1:
        return 1.50
    elif coffee == 2:
        return 2.50
    else:
        return 3.00

def reportForMachine(water=300, milk=200, coffee=100):
    print("The Quantity of Ingridients are as follows: ")
    
    print(f"1. Water: {water}ml")
    print(f"2. Milk: {milk}ml")
    print(f"3. Coffee: {coffee}ml")

def main():
    print("Welcome To The Coffee Shop")
    decision = displayOptions()

    while (decision != -1):
        if decision == 1:
            reportForMachine()
            break
        if decision == 2:
            selectACoffee()
            break
        if decision == 3:
            break

if __name__ == "__main__":
    main()
