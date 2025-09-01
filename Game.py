import random

rock = 1
paper = 2
scissors = 3

def user_choice():
    while True:
        try:
            user_input = int(input("Enter your choice(1: Rock, 2: Paper, 3: Scissors):  "))
            if user_input in [rock,paper,scissors]:
                return user_input
            else:
                return "Invalid choice. Please choose 1, 2, or 3."
        except ValueError:
            return "Invalid input. Please enter a number."
        
def computer_choice():
    return random.randint(1,3)

def determine_winnner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == rock and computer_choice == scissors) or \
         (user_choice == paper and computer_choice == rock) or \
         (user_choice == scissors and computer_choice == paper):
        return "You win!"
    else:
        return "Computer wins!"

# --- Main Game Loop ---
print("🎮 Welcome to Rock-Paper-Scissors!")

# Scoreboard
score = {"user": 0, "computer": 0, "ties": 0}

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {choice_to_string(user_choice)}")
    print(f"Computer chose: {choice_to_string(computer_choice)}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
        score["ties"] += 1
    elif winner == "user":
        print("You win!")
        score["user"] += 1
    else:
        print("Computer wins!")
        score["computer"] += 1

    # Display scoreboard
    print("\n📊 Scoreboard:")
    print(f"You: {score['user']} | Computer: {score['computer']} | Ties: {score['ties']}")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("\nFinal Scoreboard:")
        print(f"You: {score['user']} | Computer: {score['computer']} | Ties: {score['ties']}")
        print("Thanks for playing! 👋")
        break