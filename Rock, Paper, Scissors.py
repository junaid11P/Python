import random

# Game options (as a dictionary for easy modification)
options = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

# Get user input
def get_user_choice():
  while True:
    user_choice = input("Enter Rock (R), Paper (P), or Scissors (S): ").upper()
    if user_choice in options.keys():
      return user_choice
    else:
      print("Invalid input. Please enter R, P, or S.")

# Generate computer's choice
def get_computer_choice():
  return random.choice(list(options.keys()))

# Determine winner
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Tie"
  elif (user_choice == "R" and computer_choice == "S") or (user_choice == "P" and computer_choice == "R") or (user_choice == "S" and computer_choice == "P"):
    return "You Win!"
  else:
    return "You Lose!"

# Play the game
def play_game():
  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(f"You chose {options[user_choice]}.")
    print(f"Computer chose {options[computer_choice]}.")
    print(result)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
      break

# Start the game
play_game()

print("Thanks for playing!")
