import random
def guessing_game():
    number_to_guess = random.randint(1,10)
    attempts = 0
    guess = None
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")           
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("⚠ Please enter a valid number.")
guessing_game()