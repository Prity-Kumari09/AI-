#Create a program that implements a simple version of the "Guess the Number" game using binary search for efficient guessing.
import random

def guess_the_number():
    """
    Play the "Guess the Number" game using binary search
    """
    # Set the range of possible numbers
    low = 1
    high = 100

    # Generate a random number within the range
    secret_number = random.randint(low, high)

    # Initialize the number of guesses
    num_guesses = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You can guess the number, and I'll tell you if you're too high or too low.")

    while True:
        # Calculate the midpoint of the range
        mid = (low + high) // 2

        # Ask the user if the midpoint is the correct number
        print(f"Is the number {mid}?")

        # Get the user's response
        response = input("Enter 'h' if the number is too high, 'l' if it's too low, or 'c' if it's correct: ")

        # Update the range based on the user's response
        if response == 'h':
            high = mid - 1
        elif response == 'l':
            low = mid + 1
        elif response == 'c':
            print(f"Yay! I guessed the number in {num_guesses + 1} attempts.")
            break
        else:
            print("Invalid response. Please try again.")

        # Increment the number of guesses
        num_guesses += 1

# Call the game function
guess_the_number()