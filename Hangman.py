import random

words = ["apple", "banana", "grape", "mango", "orange"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
chances = 6

print("Welcome to Hangman")

while chances > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Chances left:", chances)
    
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Letter already guessed")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess")
        chances -= 1

if "_" not in guessed_word:
    print("You won. The word was:", word)
else:
    print("You lost. The word was:", word)
