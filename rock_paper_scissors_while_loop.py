import random

user_score = 0
computer_score = 0
max_score = 5

while True:
    user_input = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_actions = random.choice(possible_action)
    if user_input.lower() == "quit":
        print("Thank you for playing.")
        exit()
    if user_input.lower() not in possible_action:
        print("Invalid action")
        continue
    print(f"\nYou chose {user_input}, computer chose {computer_actions}.\n")
    # BODY SOURCE CODE
    if user_input.lower() == computer_actions:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input.lower() == "rock":
        if computer_actions == "scissors":
            print(f"Rock smashes scissors! You win!")
        else:
            print(f"Paper covers rock! You lose.")
    elif user_input.lower() == "paper":
        if computer_actions == "rock":
            print("Paper covers rock! You win!")
        else:
            print(f"Scissors cuts paper! You lose.")
    elif user_input.lower() == "scissors":
        if computer_actions == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    # USER AND COMPUTER SCORE CODE
    if user_input.lower() == "rock" and computer_actions == "scissors":
        user_score += 1
    elif user_input.lower() == "scissors" and computer_actions == "paper":
        user_score += 1
    elif user_input.lower() == "paper" and computer_actions == "rock":
        user_score += 1
    elif user_input.lower() == computer_actions:
        user_score += 0
        computer_score += 0
        # print("No points added, please keep playing.")
    else:
        computer_score += 1
    # FINAL SCORE CALCULATIONS
    if user_score >= max_score:
        print(f"Congratulations you win! You have {user_score} points vs {computer_score} points." )
        break
    if computer_score >= max_score:
        print(f"You lose. Computer wins! Computer have {computer_score} points vs {user_score} points.")
        break
    if user_score == max_score and computer_score == max_score:
        print(f"No winners! \nYou have {user_score} points. \nComputer have {computer_score} points.")
        break

    play_again = input("Play again? (Yes/No): ")
    if play_again.lower() != "yes":
        if user_score > computer_score:
            print(f"Thank you for playing. Final score is {user_score} point/s vs {computer_score} point/s. You win!")
        elif user_score == computer_score:
            print(f"Thank you for playing. Final score is {user_score} point/s vs {computer_score} point/s. It's a tie!")
        else:
            print(f"Thank you for playing. Final score is {user_score} point/s vs {computer_score} point/s. Computer win!")
        break
