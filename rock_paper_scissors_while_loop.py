import random

while True:
    user_input = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_actions = random.choice(possible_action)
    if user_input not in possible_action:
        print("Invalid action")
        continue
    print(f"\nYou chose {user_input}, computer chose {computer_actions}.\n")

    if user_input == computer_actions:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_actions == "scissors":
            print(f"Rock smashes scissors! You win!")
        else:
            print(f"Paper covers rock! You lose.")
    elif user_input == "paper":
        if computer_actions == "rock":
            print("Paper covers rock! You win!")
        else:
            print(f"Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_actions == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (Yes/No): ")
    if play_again.lower() != "yes":
        break
