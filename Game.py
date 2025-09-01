import random

rock = 1
paper = 2
scissors = 3
win = 0
loss = 0
tie = 0
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
    global win, loss, tie
    if user_choice == computer_choice:
        tie = tie + 1
        return "It's a tie!"
    elif (user_choice == rock and computer_choice == scissors) or \
         (user_choice == paper and computer_choice == rock) or \
         (user_choice == scissors and computer_choice == paper):
        win = win + 1
        return "You win!"
    else:
        loss = loss + 1
        return "Computer wins!"

# --- Main Game Loop ---
print("🎮 Welcome to Rock-Paper-Scissors!")

while True:
    user_input = user_choice()
    computer_choicee = computer_choice()
    print("\nYou chose: "+str(user_input))
    print("Computer chose: "+str(computer_choicee))
    print(determine_winnner(user_input, computer_choicee))
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! 👋")
        break
    
def score_board():
    print("Scoreboard - Wins: "+str(win)+", Losses: "+str(loss)+", Ties: "+str(tie)) 
score_board()
