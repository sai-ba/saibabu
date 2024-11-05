import random

def hangman_game():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    while attempts > 0:
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Guesses left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            attempts -= 1
            print("Incorrect guess.")

    print(f"Sorry, you ran out of attempts. The word was: {word}")

hangman_game()
