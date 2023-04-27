import random

print("Welcome To Rock Paper Scissor")

humanChoice = int(input("What Do You Chose? (0 for rock, 1 for paper, 2 for scissor): "))
computerChoice = random.randrange(1,3) - 1

if (humanChoice == 0 and computerChoice == 0) or (humanChoice == 1 and computerChoice == 1) or (humanChoice == 2 and computerChoice == 2):
    print("Draw")
elif (humanChoice == 0 and computerChoice == 1) or (humanChoice == 1 and computerChoice == 2) or (humanChoice == 2 and computerChoice == 0):
    print("Computer Wins")
elif (humanChoice == 0 and computerChoice == 2) or (humanChoice == 1 and computerChoice == 0) or (humanChoice == 2 and computerChoice == 1):
    print("Human Wins")
else:
    print("Invalid Input")