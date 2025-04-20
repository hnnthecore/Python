# Exercise 02: Guess the Number Game

# Secret number to guess
secret_number = 7
guess = None

print("I'm thinking of a number between 1 and 10...")

# Keep looping until the guess is correct
while guess != secret_number:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
