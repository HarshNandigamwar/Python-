word = "apple"
guessed = ['_'] * len(word)
attempts = 6

print("Welcome to the Word Guessing Game!")
print("Guess the 5-letter word.")

while attempts > 0 and ''.join(guessed) != word:
    print("\nWord:", ' '.join(guessed))
    print(f"Attempts left: {attempts}")
    guess = input("Enter a letter: ").lower()

    if guess in word:
        correct = False
        for i in range(len(word)):
            if word[i] == guess and guessed[i] == '_':
                guessed[i] = guess
                correct = True
        if not correct:
            print("You already guessed that letter.")
    else:
        print("Wrong guess!")
        attempts -= 1

if ''.join(guessed) == word:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame Over! The word was: {word}")
