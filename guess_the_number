#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#import art
import random

def comparison(num, guessing):
  if guessing > num:
    print("Too high. \nGuess again.")
  elif guessing < num:
    print("Too low. \nGuess again.")

#print(art.logo)
difficulty = input(f"Welcome to the number guessing game! \nI'm thinking of a number from 1 and 100! \nChoose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5

genNum = random.randint(1,100)
while attempts > 0:
  guess = int(input(f"You have {attempts} guesses. What is your guess?: "))
  if guess == genNum:
    print(f"Congrats, you guessed the number, {genNum}! :D")
    break  # Exit the loop if the guess is correct
  else:
    comparison(genNum, guess)
    attempts -= 1
if attempts == 0:
  print(f"You are all out of attempts, {attempts} left.")
