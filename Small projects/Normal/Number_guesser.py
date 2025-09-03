#Setting up the setup
import random
number_picked = random.randint(1, 10)
guess = int(input("Enter a number between 1 and 10: "))

#Conditional statements
if guess == number_picked:
    print("Hey you got it correct, here have a cookie -> 🍪")
elif guess > 10 or guess < 1:
    print("It's between 1 and 10 or equal to them")
else:
    print(f"Nope, it's wrong! The number is {number_picked}")

