import art
import game_data
import random
from replit import clear

def rand_big(contended):
  """returns the 'data' list number of a fresh random 'big deal' from the game data list."""
  big_list_len = len(game_data.data) - 1
  big_pick = random.randint(0,big_list_len)
  # in the case that the pick has been seen before on the contended list, the function repeats, this time assigning the output to big_pick
  if big_pick in contended:
    big_pick = rand_big(contended)
  return big_pick

def big_align(biggie):
  """returns the name, description, country, and follower count of the 'big deal' so that they may be saved to variables"""
  return (
    game_data.data[biggie]["name"],
    game_data.data[biggie]["description"],
    game_data.data[biggie]["country"],
    game_data.data[biggie]["follower_count"]
  )

def higher_or_lower():
  contended = []
  # Assigns the first random big deal
  bigA = rand_big(contended)
  contended.append(bigA)
  # Assigns the second random big deal
  bigB = rand_big(contended)
  contended.append(bigB)
  winStreak = 0
  #as long as the player guesses correctly, the game continues
  player_streak = True

  while player_streak:
    # Re-assigns values to our important variables with our new contenders
    bigA_name, bigA_description, bigA_country, bigA_count = big_align(bigA)
    bigB_name, bigB_description, bigB_country, bigB_count = big_align(bigB)

    print(art.logo)

    # After the first loop the player's score will be tracked and printed
    if winStreak > 0:
      print(f"You're right! Current score: {winStreak}")
    
    print(f"Compare A: {bigA_name}, a {bigA_description}, from {bigA_country}.")
    print(art.vs)
    print(f"Against B: {bigB_name}, a {bigB_description}, from {bigB_country}.")
  
    player_pick = input(f"Who has more followers? Type 'A' or 'B': ").lower()
  
    if player_pick == "a" and bigA_count > bigB_count:
      winStreak += 1
      # replaces the losing contender B
      bigB = rand_big(contended)
      contended.append(bigB)
      clear()
    elif player_pick == "b" and bigA_count < bigB_count:
      winStreak += 1
      # changes A to the winner (B) and generates a new B
      bigA = bigB
      bigB = rand_big(contended)
      contended.append(bigB)
      clear()
    elif player_pick == "a" and bigA_count < bigB_count or player_pick == "b" and bigA_count > bigB_count:
      # if the player is wrong, the game ends
      clear()
      print(art.logo)
      print(f"Sorry that's wrong. Final score: {winStreak}")
      player_streak = False

higher_or_lower()
