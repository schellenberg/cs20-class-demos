import random

# generate a random number from 1 to 100
secret_number = random.randrange(1, 101)

# count how many guesses the player has made
tries = 0
# keep looping until the player guesses the exact number
still_guessing = True

while still_guessing:
    # get the user to guess the number
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1

    # compare the guess with the secret number and give a hint
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        # stop the loop when the guess is correct
        still_guessing = False

print(f"Way to go! You guessed the right number in {tries} tries!")