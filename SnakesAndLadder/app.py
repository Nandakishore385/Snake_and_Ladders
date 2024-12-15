import random

# Board configuration with ladders and snakes
board = {
    3: 22,   # Ladder from 3 to 22
    5: 8,    # Ladder from 5 to 8
    11: 26,  # Ladder from 11 to 26
    20: 29,  # Ladder from 20 to 29
    17: 4,   # Snake from 17 to 4
    19: 7,   # Snake from 19 to 7
    27: 1,   # Snake from 27 to 1
    21: 9,   # Snake from 21 to 9
}

def roll_dice():
    """Simulate rolling a 6-sided dice."""
    return random.randint(1, 6)

def play_snake_and_ladders():
    print("Welcome to Snake and Ladders!")
    position = 0
    
    while position < 30:  # Game ends when the player reaches position 30
        input("\nPress Enter to roll the dice...")
        dice = roll_dice()
        print(f"You rolled a {dice}!")
        
        # Update the position
        position += dice
        if position > 30:
            print("Roll exceeds the last square, try again!")
            position -= dice
            continue
        
        print(f"You moved to position {position}.")
        
        # Check for snakes or ladders
        if position in board:
            if position < board[position]:
                print(f"Ladder! Climb up to {board[position]}!")
            else:
                print(f"Snake! Slide down to {board[position]}!")
            position = board[position]
        
        print(f"Current position: {position}")
    
    print("\nCongratulations! You reached the end of the board!")

# Run the game
if _name_ == "_main_":
    play_snake_and_ladders()