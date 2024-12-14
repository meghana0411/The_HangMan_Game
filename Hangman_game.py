import random

fruits = ["orange", "watermelon", "strawberry", "apple", "banana", "mango", "grapes", "kiwi", "cherry", "apricot", "papaya", "guava"]
chosen_word = random.choice(fruits).lower()

guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count = 0

hangman_stages = [
    """
  +-----+
    |   |
        |
        |
        |
        |
       
    =========""",
    """
  +-----+
    |   |
    o   |
        |
        |
        |
    =========""",
    """ 
  +-----+
    |   |
    o   |
    |   |
        |
        |
  =========""",
    """
  +-----+
    |   |
    o   |
    |\  |
        |
        |
  =========""",
    """
  +-----+
    |   |
    o   |
   /|\  |
        |
        |
  =========""",
    """
  +-----+
    |   |
    o   |
   /|\  |
   /    |
        |
  =========""",
    """ 
  +-----+
    |   |
    o   |
   /|\  |
   / \  |
        |
  ========="""
]

while tries > 0:
    output = ""
    for letter in chosen_word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += "_"

    if output == chosen_word:
        print("You have guessed the fruit and you win !!!")
        break

    print("Guess the fruit: ", " ".join(output))
    print(tries, "chances left")
    guess = input("Enter your guess: ").lower()

    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed", guess)
    elif guess in chosen_word:
        print("Awesome! You have guessed the correct letter.")
        guessed_correctly.append(guess)
    else:
        print("Sorry! You have guessed a wrong letter!")
        hangman_count += 1
        tries -= 1
        guessed_incorrectly.append(guess)
        print(hangman_stages[hangman_count])

if tries == 0 and output != chosen_word:
    print("Sorry, you guessed wrong. The word was:", chosen_word, "Play again!")
