import random
print("What's your guess?")

word = random.choice(["word","world","city"])
guesses = ''

turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed = failed + 1
    if failed == 0:
        print("You won")

        break

    guess = input("guess a character:")
    guesses = guess + guesses

    if guess not in word:

        turns = turns - 1

        print("Wrong")

        print("You have", + turns, "more guesses")

        if turns == 0:
            print("You lost, sorry")