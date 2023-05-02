from utilities import celebrities

def startTheGame():
    print("Welcome To Higher or Lower!")
    print("Correctly Guess Who Has More IG Followers!")
    
def startComparing():
    score = 0
    for i in range(len(celebrities.items())):
        first = list(celebrities.keys())[i]
        second = list(celebrities.keys())[i+1]
        
        firstDescription = list(celebrities.values())[i][0]
        secondDescription = list(celebrities.values())[i+1][0]
        
        firstFollowers = list(celebrities.values())[i][1]
        secondFollowers = list(celebrities.values())[i+1][1]
        
        print(f"Compare A: {first}, {firstDescription}")
        print(f"Against B: {second}, {secondDescription}")

        decision = input("Who Has More IG Followers? (Press A for Option A and B for Option B): ")
        if decision == 'A' and firstFollowers > secondFollowers:
            score += 1
            print(f"Correct Guess. Score: {score}")
            continue
        elif decision == 'B' and secondFollowers > firstFollowers:
            score += 1
            print(f"Correct Guess. Score: {score}")
        elif decision == 'A' and secondFollowers > firstFollowers:
            print(f"Wrong Guess. Score: {score}")
            break
        elif decision == 'B' and firstFollowers > secondFollowers:
            print(f"Wrong Guess. Score: {score}")
            break
        else:
            print("Invalid Input")
            break

def main():
    startTheGame()
    startComparing()

if __name__ == '__main__':
    main()
