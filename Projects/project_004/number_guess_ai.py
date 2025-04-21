# Project 004: Number Guessing Game (AI guesses)

print("Think of a number between 1 and 100.")
input("Press Enter when you're ready...")

low = 1
high = 100
guesses = 0

while True:
    guess = (low + high) // 2
    guesses += 1
    print(f"My guess is: {guess}")

    feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1
    elif feedback == "c":
        print(f"Yay! I guessed it in {guesses} tries!")
        break
    else:
        print("Invalid input. Please type H, L, or C.")
