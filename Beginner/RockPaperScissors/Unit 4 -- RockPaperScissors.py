import random

rules = """
1. Two players: You vs. the Computer.
2. Each player chooses one of the following:
   - Rock (🪨)
   - Paper (📄)
   - Scissors (✂️)
3. Both choices are revealed at the same time.
4. The outcome is determined as follows:
   - Rock crushes Scissors → Rock wins
   - Scissors cut Paper → Scissors win
   - Paper covers Rock → Paper wins
   - Same choice → Tie (draw)
"""

rock = """
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
 _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
 __      __
( _\\    /_ )
 \\ _\\  /_ / 
  \\ _\\/__/_ _ 
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \\/  ;   /
    | === |
"""

choices = ["rock", "paper", "scissors"]
choices_ascii = [rock, paper, scissors]

print("Welcome to Rock-Paper-Scissors Game!")

computer_choice = random.choice(choices)
computer_choice_ascii = choices_ascii[choices.index(computer_choice)]

user_choice = input("What do you choose? (Rock, Paper, or Scissors): ").lower()

#Check validity before using index
if user_choice not in choices:
    print("Invalid choice!")
else:
    user_choice_ascii = choices_ascii[choices.index(user_choice)]

    if computer_choice == user_choice:
        print(f"DRAW!\nBoth of you chose {user_choice}\n{user_choice_ascii}\n{computer_choice_ascii}")
    else:
        if computer_choice == "rock" and user_choice == "paper":
            print(f"You won!!\nComputer chose: {computer_choice}\n{computer_choice_ascii}")
            print(f"You chose: {user_choice}\n{user_choice_ascii}")
            print("The paper covers the rock.")

        elif computer_choice == "paper" and user_choice == "rock":
            print(f"You lost!!\nComputer chose: {computer_choice}\n{computer_choice_ascii}")
            print(f"You chose: {user_choice}\n{user_choice_ascii}")
            print("The paper covers the rock.")

        elif computer_choice == "scissors" and user_choice == 'paper':
            print(f"You lost!!\nComputer chose: {computer_choice}\n{computer_choice_ascii}")
            print(f"You chose: {user_choice}\n{user_choice_ascii}")
            print("The scissors cut the paper.")

        elif computer_choice == "paper" and user_choice == "scissors":
            print(f"You won!!\nComputer chose: {computer_choice}\n{computer_choice_ascii}")
            print(f"You chose: {user_choice}\n{user_choice_ascii}")
            print("The scissors cut the paper.")

        elif computer_choice == "scissors" and user_choice == "rock":
            print(f"You won!!\nComputer chose: {computer_choice}\n{computer_choice_ascii}")
            print(f"You chose: {user_choice}\n{user_choice_ascii}")
            print("The rock cracks the scissors.")

        elif computer_choice == "rock" and user_choice == "scissors":
            print(f"You lost!!\nComputer chose: {computer_choice}\n{computer_choice_ascii}")
            print(f"You chose: {user_choice}\n{user_choice_ascii}")
            print("The rock cracks the scissors.")
