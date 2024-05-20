# Overview
This is a Python implementation of the popular word-guessing game Wordle. The game randomly selects a five-letter word from a predefined list of words, and the player has six attempts to guess it. The game provides feedback after each guess by coloring the letters:

* **Green:** The letter is correct and in the correct position.
* **Yellow:** The letter is correct but in the wrong position.
* **Grey:** The letter is not in the word.

# Features
* **Color-coded feedback:** Uses ANSI escape codes to color the output in the terminal.
* **Real word check:** Uses an online dictionary API to validate words.
* **QWERTY keyboard display:** Shows the state of the virtual keyboard with color-coded feedback.

# Dependencies
* Python 3.x
* requests library for API calls

# Installation
1. Clone the repository or download the source code.
2. Install the required dependencies: "pip install requests"
3. Make sure you have a file named words.txt in the same directory as the script, containing a list of valid five-letter words.

# How to Play
1. Run the script: "python wordle.py"
2. The game will select a random word from words.txt.
3. Enter your five-letter guess when prompted.
4. The game will provide feedback using colors:
- Green for correct letters in the correct position.
- Yellow for correct letters in the wrong position.
- Grey for letters not in the word.
5. You have six attempts to guess the word correctly.
# 

Enjoy playing Wordle! If you have any questions or issues, feel free to reach out.
