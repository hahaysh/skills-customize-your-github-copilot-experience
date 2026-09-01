
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic word-guessing game using Python strings, loops, conditionals, user input, and random selection. Players must reveal a hidden word before they run out of incorrect guesses.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Use the provided starter code to select a secret word and initialize the values needed to track the game.

#### Requirements
Completed program should:

- Randomly select one secret word from the predefined `words` list.
- Store guessed letters in a collection that can be updated during the game.
- Set and track a maximum number of incorrect guesses.

### 🛠️ Build the Guessing Loop

#### Description
Create the main game loop so the player can enter letters, view their progress, and receive a final result.

#### Requirements
Completed program should:

- Accept one letter guess from the player during each turn.
- Display guessed letters in their correct positions and underscores for letters that have not been guessed, such as `_ _ t`.
- Update and display the number of incorrect guesses remaining.
- End when the player reveals the entire word or uses all allowed incorrect guesses.
- Display a clear win or loss message and reveal the secret word when the game ends.
