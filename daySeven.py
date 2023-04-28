import random

wordList = ["camel", "baboon", "ape"]

lives = 7
endOfGame = False

word = random.choice(wordList)
wordLength = len(word)

display = []
for _ in range(wordLength):
    display += "_"

while endOfGame is False:
    guess = input("Guess A Letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter. No Life Lost.")

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:    
            display[position] = letter 
    
    if guess not in display:
        print(f"You have not guessed the letter. You lost a Life.")
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You Lose")
            break
    
    print(f"{' '.join(display)}")

    if '_' not in display:
        print("You Win. Congratulations.")
        break
