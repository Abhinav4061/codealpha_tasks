import random

words = ["python", "apple", "computer", "school", "garden"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=== Welcome to Hangman ===")

while wrong_guesses < max_wrong and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

    guess = input("Enter a letter: ").lower().strip()
    
    # FIX 1: Validate input (must be exactly one alphabetic character)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guess is in the secret word
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong!")
        wrong_guesses += 1

# Game Over / Win Check
if "_" not in guessed_word:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print("\nGame Over!")
    print(f"The word was: {word}")
