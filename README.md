# Number Guessing Game
## Description
This is a simple number guessing game where the player tries to guess a randomly generated number between 1 and 100. The game provides hints ("Higher" or "Lower") after each incorrect guess and keeps track of the number of attempts. At the end, it compares the player's score with the current high score stored in a file.

## Features
Random number generation between 1 and 100

Real-time feedback (Higher/Lower) for each guess

Attempt counter

High score tracking (reads from and writes to a file)

Celebration message when a new high score is achieved

## How to Play
Run the main.py file using Python

Enter your guess when prompted

Receive feedback on whether your guess was too high or too low

Continue guessing until you find the correct number

The game will display your total attempts and check if you've set a new high score

## Requirements
Python 3.x

A file named hiscore.txt in the same directory containing a valid integer (create one manually if it doesn't exist)

## Note
The current code attempts to write the new high score to "hiscore2.txt" instead of updating "hiscore.txt". You may want to modify this to use the same file for consistency.
