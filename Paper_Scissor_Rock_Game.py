import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    
    # Initialize scores
    user_score = 0
    computer_score = 0

    while True:
        # Step 1: User input
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please select rock, paper, or scissors.")
            continue

        # Step 2: Computer selection
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        # Step 3: Determine the winner
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display scores
        print(f"Score: You {user_score} - {computer_score} Computer")

        # Step 4: Ask if the user wants to play again
        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Start the game
play_game()

