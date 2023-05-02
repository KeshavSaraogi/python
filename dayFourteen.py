from utilities import celebrities

def startTheGame():
    print("Welcome To Higher or Lower!")
    print("Correctly Guess Who Has More IG Followers!")
    

def startComparing():
    first = list(celebrities.keys())[0]
    second = list(celebrities.keys())[1]

    firstDescription = list(celebrities.values())[0][0]
    secondDescription = list(celebrities.values())[1][0]

    firstFollowers = list(celebrities.values())[0][1]
    secondFollowers = list(celebrities.values())[1][1]
    #print(firstDescription, secondDescription)
    
    print(f"Compare A: {first}, {firstDescription}")
    print(f"Against B: {second}, {secondDescription}")

    decision = input("Who Has More IG Followers? (Press A for Option A and B for Option B): ")
    if decision == 'A' and firstFollowers > secondFollowers:
        print("Correct Decision")
    elif decision == 'B' and secondFollowers > firstFollowers:
        print("Correct Decision")
    else:
        print("Invalid Guess")

def main():
    startTheGame()
    startComparing()

if __name__ == '__main__':
    main()
