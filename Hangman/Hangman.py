import random

# List of words for the game
word_list = ["python", "programming", "hangman", "developer", "keyboard", "algorithm"]

# Choose a random word
word = random.choice(word_list)
guessed_letters = []
tries = 6  # Number of allowed wrong guesses

print("🎯 Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print(f"❌ Wrong guess! You have {tries} tries left.")

    # Show current word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("\n💀 Game Over! The word was:", word)
