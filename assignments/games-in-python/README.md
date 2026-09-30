# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in Python to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Create the game data and display the hidden word so the player can begin guessing.

#### Requirements
Completed program should:

- Store at least five possible words in a predefined list.
- Randomly select one word at the beginning of each game.
- Display one underscore for each unguessed letter in the selected word.
- Give the player six incorrect guesses before the game ends.

### 🛠️	Process Guesses and Determine the Result

#### Description
Prompt the player for letters, update the game after each guess, and continue until the player wins or runs out of guesses.

#### Requirements
Completed program should:

- Accept one letter at a time and reject entries that are not a single alphabetic character.
- Reveal every matching position when the player guesses a letter correctly.
- Track guessed letters and notify the player when a letter has already been entered.
- Reduce the remaining guesses only when the player enters a new incorrect letter.
- Display the current word progress and remaining guesses after each valid guess.
- End with a clear win message when the word is completed or a loss message that reveals the word when no guesses remain.
