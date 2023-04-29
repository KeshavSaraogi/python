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
        while endTheGame is False:
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
            print("Computer Cards Are: " + str(computerCards) + " \nComputer Score Is: " + str(computerScore))

            if humanScore > 21:
                endTheGame = True
            elif computerScore > 21:
                endTheGame = True
            else:
                card = getAnotherCard()
                if card == 'n':                                         
                    #simulate computer and calculate winner
                    #make sure the human score and computer score is below 21
                    #get cards for computer, maximum one more than human 
                    #if he reaches a higher score but less than 21, computer wins
                    #but if the score is above 21, computer losess
                    pass
                if card == 'y':                                         
                    #continue to provide cards and later simulate computer and calculate winner 
                    #until the cards come up to 21, the human can hit
                    #as soon as the human asks for a pass, we go back to the computer.               
                    pass

if __name__ == "__main__":
    main()
