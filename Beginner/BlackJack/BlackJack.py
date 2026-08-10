import random
import os
import time

def clear_screen():
    time.sleep(1)
    os.system('cls') if os.name == 'nt' else os.system('clear')

def rules():
    print("""
                ### Precaution ###
        # This game (Blackjack) is haram to play for real money or entertainment in Islam.
        # Use its concept *only* for programming practice.
          
        - The goal of the game is to reach a total of 21, or get as close as possible and without exceeding it!
        - The user plays against the computer.
        - The user receives 2 visible cards showing their values.
        - The computer also receives 2 cards: one visible, one hidden.
        - The cards 2–10 are worth their face value.
        - Face cards (Jack, Queen, King) each equal 10.
        - You decide whether the Ace (A) counts as 1 or 11.

        If both player and computer reach 21, it's a draw.
        “BlackJack” happens when you hit 21 with the first two cards.

        The computer keeps drawing cards until it reaches 17.
        Once 17 or more, it stops drawing.
    """)
    input("Press Enter to start the game... ")
    os.system('cls') if os.name=='nt' else os.system('clear')

def new_card():
    cards = {
        "A": [1, 11],
        "2": [2], "3": [3], "4": [4], "5": [5], "6": [6],
        "7": [7], "8": [8], "9": [9], "10": [10],
        "J": [10], "Q": [10], "K": [10]
    }
    cards_list = list(cards.keys())
    card = random.choice(cards_list)
    return card, cards[card]

def cards_value(cards):
    total = 0
    aces = 0
    for card, values in cards:
        if card == "A":
            aces += 1
            total += 11
        else:
            total += values[0]

    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def display_cards(owner, cards, hide_second=False):
    if hide_second:
        print(f"{owner}'s cards: [{cards[0][0]}, ?]")
    else:
        shown = ', '.join(card for card, _ in cards)
        print(f"{owner}'s cards: [{shown}] → Total: {cards_value(cards)}")

def blackjack():
    clear_screen()
    temp=input("Do you want to see the rules? (y/n) ").lower()
    if temp=='y':
        rules()
    else:
        input("Press enter to continue: ")
        clear_screen()

    player_cards = [new_card(), new_card()]
    computer_cards = [new_card(), new_card()]

    display_cards("Your", player_cards)
    display_cards("\nComputer", computer_cards, hide_second=True)

    while True:
        total = cards_value(player_cards)
        if total == 21:
            print("BlackJack! You hit 21!")
            break
        elif total > 21:
            print("You went over 21. You lose.")
            return

        move = input("\nDo you want to draw another card (y/n)? ").lower()
        if move == "y":
            player_cards.append(new_card())
            display_cards("Your", player_cards)
        elif move == "n":
            break
        else:
            print("Invalid input. Use 'y' or 'n'.")

    print("\nComputer's turn...")
    display_cards("Computer", computer_cards)
    while cards_value(computer_cards) < 17:
        print("Computer draws a card...")
        time.sleep(1)
        computer_cards.append(new_card())
        display_cards("Computer", computer_cards)

    player_total = cards_value(player_cards)
    computer_total = cards_value(computer_cards)

    print("\n\n--- Final Results ---")
    display_cards("Your", player_cards)
    display_cards("Computer", computer_cards)

    if computer_total > 21 or player_total > computer_total:
        print("\nYou win!")
    elif player_total < computer_total:
        print("\nComputer wins.")
    else:
        print("\nDraw.")

    input("\n\nPress Enter to return to main menu...")
    clear_screen()

def games():
    print("""
    Choose a game to start with: 
        1. Snake
        2. Twenty One (BlackJack)
        3. PingPong
        4. Exit
    -----------------------------
    """)
    choice = input("Please enter a digit: ")
    while not choice.isdigit():
        choice = input("Please enter a digit: ")
    return int(choice)

while True:
    choice = games()

    if choice == 1:
        print("Coming Soon!")
        clear_screen()
    elif choice == 2:
        blackjack()
    elif choice == 3:
        print("Coming Soon!")
        clear_screen()
    elif choice==4:
        print("Exiting...")
        clear_screen()
        break
    else:
        print("Invalid option.")
        clear_screen()
