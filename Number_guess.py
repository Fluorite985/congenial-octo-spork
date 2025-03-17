import random

def welcome():#welcoming the player
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\nCan you guess it?")

def generate_random_number():#generate a random number
    return random.randint(1, 100)  

def choosing_difficulty():#selecting number of tries
    while True:
        difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "medium":
            return 5
        elif difficulty == "hard":
            return 3
        else:
            print("Invalid input. Please try again.")

def play_game():#the main game
    welcome()
    secret_number = generate_random_number() 
    tries = choosing_difficulty()
    attempts = 0
    print(f"You have {tries} attempts to guess the number!")

    while attempts < tries:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
        
        if attempts == tries:
            print("You are out of tries! Game over!")
            print(f"The number was {secret_number}")
            break  

    play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing! Goodbye!")

def main():#run the game
    play_game()

if __name__ == "__main__":
    main()
