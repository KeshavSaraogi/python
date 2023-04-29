import random

cards = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, 
        "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

def play():
    decision = input("Do You Want To Play A Game of Blackjack? (y/n): ")
    return decision

def generateInitialComputerCards():
    firstComputerCard = random.choice(list(cards.keys()))
    return firstComputerCard

def generateInitialHumanCards():
    firstHumanCard = random.choice(list(cards.keys()))
    secondHumanCard = random.choice(list(cards.keys()))
    return firstHumanCard, secondHumanCard

def generateCard():
    card = random.choice(list(cards.keys()))
    return card

def calculateScore(li):
    score = 0
    for i in li:
        score += cards[i]
    return score

def getAnotherCard():
    direction = input("Do You Want To Get Another Card? (y/n): ")
    return direction

def main():
    print("Welcome To Blackjack!")
    endTheGame = False

    decision = play()
    if decision == 'n':
        exit
    else:
        humanScore = 0
        computerScore = 0
        humanCards = []
        computerCards = []
        
        cFirst = generateInitialComputerCards()
        hFirst, hSecond = generateInitialHumanCards()
        
        humanCards.append(hFirst)
        humanCards.append(hSecond)
        computerCards.append(cFirst)

        humanScore = calculateScore(humanCards)
        computerScore = calculateScore(computerCards)

        print("Your Cards Are: " + str(humanCards) + " \nYour Score Is: " + str(humanScore))
        print("Computers First Card Is: " + str(computerCards) + " \nComputer Score Is: " + str(computerScore))

        while (endTheGame is False):
            direction = input("Press 'h' for Hit or press 'p' for Pass: ")
            if direction == 'h':
                card = generateCard()
                humanCards.append(card)
                humanScore = calculateScore(humanCards)

                print(humanCards)
                print("Your Score Is: " + str(humanScore))

                if int(humanScore == 21):
                    print("You Hit 21. You Won The Game")
                    endTheGame = True

                if int(humanScore) > 21:
                    print("Your Score Is Above 21. You lost.")
                    endTheGame = True
            elif direction == 'p':
                while (computerScore <= 21):

                    card = generateCard()
                    computerCards.append(card)
                    computerScore = calculateScore(computerCards)

                    print(computerCards)
                    print("Computer Score Is: " + str(computerScore))
                
                    if int(computerScore) > humanScore and int(computerScore) < 21:
                        print("Computer Wins.")
                        endTheGame = True
                    elif (int(computerScore) > 21):
                        print("Computer Score Is Above 21. You Win.")
                        endTheGame = True
if __name__ == "__main__":
    main()
