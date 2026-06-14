import random

words = ["python", "apple", "tiger", "robot", "music"]

secret_word = random.choice(words)

guessed_word = ["_"] * len(secret_word)

attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in guessed_word:
    print("\nCongratulations! You Won!")
else:
    print("\nGame Over!")
    print("The word was:", secret_word)