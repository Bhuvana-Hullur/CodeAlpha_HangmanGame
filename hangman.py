import random


words = ["apple", "banana", "grape", "mango", "peach"]
word = random.choice(words)  # Randomly choose a word
hidden = ["_"] * len(word)   # Create a hidden version of the word

attempts = 6  # Maximum wrong guesses allowed
guessed = []  # List to store guessed letters

print("Welcome to Hangman!")
print("Guess the word: ", " ".join(hidden))

while attempts > 0 and "_" in hidden:
    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    print("Word:", " ".join(hidden))


if "_" not in hidden:
    print("You win! The word was:", word)
else:
    print("You lost! The word was:", word)
