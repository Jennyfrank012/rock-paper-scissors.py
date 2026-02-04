import random

# Define possible choices
choices = ["rock", "paper", "scissors"]

# Get user's choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Check if user input is valid
if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    # Generate computer's choice
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")

    else:
        print("Computer wins!")
