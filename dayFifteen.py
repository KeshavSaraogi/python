def displayOptions():
    print("Welcome to Coffee Shop")
    print("Here Are Your Options: \n1. Espresso\n2. Latte\n3. Cappuccino")
    coffee = input("Which Coffee Would You Like Today? ")
    print(coffee)

def main():
    displayOptions()

if __name__ == "__main__":
    main()