#value for coins
quarterValue = 25
dimeValue    = 10
nickelValue  = 5
pennyValue   = 1

#cost for coffee
espresso   = 1.50
lattee     = 2.00
cappuccino = 3.00

resources = {
    "espresso" : {
        "milk"   : 0,
        "water"  : 50,
        "coffee" : 18
    }, 
    "lattee" : {
        "milk"   : 200,
        "water"  : 150,
        "coffee" : 24
    }, 
    "cappuccino": {
        "milk"   : 250,
        "water"  : 100,
        "coffee" : 24
    }
}

def displayCoffeeOptions():
    print(f"Here Are Your Options: \n1. Espresso   -- ${espresso}\n2. Latte      -- ${lattee}\n3. Cappuccino -- ${cappuccino}")
    coffee = int(input("Which Coffee Would You Like Today? "))
    return coffee

def processCoins(coffeeSelection):
    if coffeeSelection > 0 and coffeeSelection < 4:
        quarters = int(input("How Many Quarters You Wish To  Enter: "))
        dimes    = int(input("How Many Dimes You Wish To Enter: "))
        nickels  = int(input("How Many Nickels You Wish To Enter: "))
        pennies  = int(input("How Many Pennies You Wish To Enter: "))

        totalAmountEntered = (quarterValue * quarters + dimeValue * dimes + nickelValue * nickels + pennyValue * pennies) / 100
        return totalAmountEntered
    else:
        print("You Entered Wrong Input For Coffee Selection.")
        print("You Are Being Exited From The Program")
        exit()

def processChangeCoins(amountEntered, coffeeSelection):
    returnChange = 0
    
    if coffeeSelection == 1:
        if float(amountEntered) > float(espresso):
            returnChange = float(amountEntered) - float(espresso)
            print(f"You Entered ${amountEntered} and your change is ${returnChange}")
        elif float(amountEntered) == float(espresso):
            print("No Change To Return")
        else:
            print(f"Insufficient Funds. Returning Your ${amountEntered}")
    
    if coffeeSelection == 2:
        if float(amountEntered) > float(espresso):
            returnChange = float(amountEntered) - float(lattee)
            print(f"You Entered ${amountEntered} and your change is ${returnChange}")
        elif float(amountEntered) == float(lattee):
            print("No Change To Return")
        else:
            print(f"Insufficient Funds. Returning Your ${amountEntered}")
    
    if coffeeSelection == 3:
        if float(amountEntered) > float(espresso):
            returnChange = float(amountEntered) - float(cappuccino)
            print(f"You Entered ${amountEntered} and your change is ${returnChange}")
        elif float(amountEntered) == float(cappuccino):
            print("No Change To Return")
        else:
            print(f"Insufficient funds. Returning Your ${amountEntered}")

def processIngridients(coffeeSelection, finalWater = 300, finalMilk   = 200, finalCoffee = 100):

    if coffeeSelection == 1:
        finalWater  = finalWater - resources["espresso"]["water"]
        finalMilk   = finalMilk - resources["espresso"]["milk"]
        finalCoffee = finalCoffee - resources["espresso"]["coffee"]

        print(f"The Resources In The Machine Are: ")
        print(f"Water: {finalWater}ML")
        print(f"Milk: {finalMilk}ML")
        print(f"Coffee: {finalCoffee}g")
        return finalWater, finalMilk, finalCoffee

    elif coffeeSelection == 2:
        finalWater  = finalWater - resources["lattee"]["water"]
        finalMilk   = finalMilk - resources["lattee"]["milk"]
        finalCoffee = finalCoffee - resources["lattee"]["coffee"]
        
        print(f"The Resources In The Machine Are: ")
        print(f"Water: {finalWater}ML")
        print(f"Milk: {finalMilk}ML")
        print(f"Coffee: {finalCoffee}g")
        return finalWater, finalMilk, finalCoffee

    else: 
        finalWater  = finalWater  - resources["cappuccino"]["water"]
        finalMilk   = finalMilk   - resources["cappuccino"]["milk"]
        finalCoffee = finalCoffee - resources["cappuccino"]["coffee"]

        print(f"The Resources In The Machine Are: ")
        print(f"Water: {finalWater}ML")
        print(f"Milk: {finalMilk}ML")
        print(f"Coffee: {finalCoffee}g")
        return finalWater, finalMilk, finalCoffee

def main():
    endTheMachine = False

    while endTheMachine is False:
        print("Welcome To The Coffee Shop")
        print("Here Are Your Options: \n1. Order Coffee\n2. Print Report\n3. Exit")
        option = int(input("Enter Your Preference: "))

        if option == 1:
            coffeeSelected = displayCoffeeOptions()
            amount = processCoins(coffeeSelected)
            processChangeCoins(amount, coffeeSelected)
            processIngridients(coffeeSelected)
        
        elif option == 2:
            processReport()
        
        elif option == 3:
            break

        else:
            print("Invalid Input")
            break

if __name__ == "__main__":
    main()
