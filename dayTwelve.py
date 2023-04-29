import random

def choseADifficulty():
    attempts = 0
    level = input("Chose A Difficulty Level (press 'e' for easy and press 'd' for difficult)? ")
    
    if level == 'd':
        attempts = 5
    else:
        attempts = 10
    return attempts, level

def generateRandomNumber():
    print("I am thinking of a number between 1 and 100")
    number = random.randint(1,100)
    return number

def startTheGame():
    print("Welcome To Number Guessing Game!")

def main():
    startTheGame()
    number = generateRandomNumber()
    numberOfAttempts, level = choseADifficulty()

    while numberOfAttempts > 0:
        print(f"The Number To Guess Is {number}")
        guess = int(input(("Enter A Guess: ")))
        if guess > number:
            print(f"Your Guess {guess} Is Too High")
            numberOfAttempts = numberOfAttempts - 1
            print(f"Number Of Attempts Left Are: {numberOfAttempts}")
        elif guess < number:
            print(f"Your Guess {guess} Is Too Low")
            numberOfAttempts = numberOfAttempts - 1
            print(f"Number Of Attempts Left Are: {numberOfAttempts}")
        else:
            print(f"You Guessed The Number {number}!")
    
    if (number != guess and numberOfAttempts == 0):
        print("You Lost The Game")

if __name__ == "__main__":
    main()