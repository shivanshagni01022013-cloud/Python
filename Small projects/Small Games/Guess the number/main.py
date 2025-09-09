import random

computerPick = random.randint(1, 100)
userGuess = int(input("Please guess a number (1-100): "))
guesses = 1

while (computerPick != userGuess):
    if userGuess > computerPick:
        userGuess = int(input("Lower number please: "))
        
    elif userGuess < computerPick:
        userGuess = int(input("Higher number please: "))

    guesses += 1
print(f"You have guessed the number {computerPick} correctly in {guesses} attempts!")
print("Thanks for playing!")
