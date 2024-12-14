# The_HangMan_Game
**Hangman Game Code Explanation:**<br>

This Python program implements a Hangman Game, where the player guesses a randomly chosen fruit by guessing its letters. The game includes a limited number of attempts and visually depicts the hangman stages as the player makes incorrect guesses. Here's a step-by-step breakdown of how the game works:

**Overview of the Game:**<br>

_Random Word Selection:_ A random fruit name is selected from a predefined list. The player must guess this word.<br>
_Player's Objective:_ The player guesses one letter at a time to reveal the hidden word within a set number of attempts.<br>
_Hangman Stages:_  Each incorrect guess adds a new part to the hangman figure. The player loses if the hangman is fully drawn before the word is guessed.<br>

**Game Variables**<br>
A list of fruits serves as the pool for the random word selection.<br>
**The game keeps track of:**<br>
_Correct Guesses:_ Letters guessed correctly and their positions in the word.<br>
_Incorrect Guesses:_ Letters guessed incorrectly.<br>
_Attempts Left:_ The number of chances remaining for the player.<br>
_Hangman Progress:_ A visual representation of the hangman figure that advances with each incorrect guess.

**Game Flow**<br>
_Initialization:_ A random fruit is selected, and placeholders (underscores) represent the unguessed letters.<br>
_Player Guesses:_ The player inputs one letter at a time:<br>
If the letter is correct, it is revealed in the word.<br>
If incorrect, it is added to the list of wrong guesses, the hangman figure progresses, and the number of attempts decreases.<br>
Already guessed letters (correct or incorrect) cannot be guessed again.<br>
_Winning Condition:_ If the player correctly guesses all the letters of the fruit, they win the game.<br>
_Losing Condition:_ If the hangman figure is completed before the word is guessed, the player loses, and the correct word is revealed.<br>

**Hangman Stages**<br>
_The hangman figure progresses through seven stages:_<br>
The gallows are drawn.<br>
The head is added.<br>
The body is drawn.<br>
One arm is added.<br>
The second arm is added.<br>
One leg is drawn.<br>
The second leg is drawn, completing the hangman.<br>

**Endgame**<br>
_Winning:_ If the guessed word matches the hidden word before the hangman figure is completed, the player wins.<br>
_Losing:_ If the player exhausts all attempts and the hangman is fully drawn, they lose, and the correct word is revealed.<br>

**How to Play**<br>
Look at the displayed underscores representing the letters of the word.<br>
_Guess a letter:_<br>
If correct, it appears in its correct position(s).<br>
If incorrect, the hangman progresses, and your remaining tries decrease.<br>
_Continue guessing until either:_<br>
You guess the entire word (win).<br>
You run out of attempts (lose).<br>

This program combines random selection, string manipulation, and a visual progression system to create an engaging guessing game. It challenges the player to deduce the word while managing their limited chances.







