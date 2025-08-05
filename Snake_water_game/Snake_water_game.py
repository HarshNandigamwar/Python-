import random

def get_computer_choice():
    return random.choice(['s', 'w', 'g'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a Draw!"
    if (user == 's' and computer == 'w') or \
       (user == 'w' and computer == 'g') or \
       (user == 'g' and computer == 's'):
        return "You Win!"
    else:
        return "Computer Wins!"

# Main Game
print("Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")
print("Enter 's' for Snake, 'w' for Water, 'g' for Gun:")

user_choice = input("Your choice: ").lower()

if user_choice not in ['s', 'w', 'g']:
    print("Invalid input! Please enter s, w, or g.")
else:
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
