# 🧩 PRODIGY_SD_02 – Guessing Game  

## 🎯 Task Overview  
This project is part of my **Prodigy Infotech Internship (Task-02)**.  
The objective of this task is to build a **Python program** that generates a random number and challenges the user to guess it.  

---

## 🧠 Project Description  
The program generates a **random number** within a specified range (1–100) and asks the user to guess it.  
For each guess, the program provides feedback on whether the guess is **too high** or **too low**.  
It continues until the user correctly guesses the number and then displays the **total number of attempts** it took to win the game.  

---

## ⚙️ Features  
✅ Generates a random number automatically  
✅ Takes user input for guessing  
✅ Gives helpful hints (too high / too low)  
✅ Tracks and displays number of attempts  
✅ Simple, interactive, and beginner-friendly  

---

## 💻 Python Code
```python
import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Can you guess it?")

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
guessing_game()

---

## EXAMPLE OUTPUT
Welcome to the Guessing Game!
I have chosen a number between 1 and 100.
Can you guess it?
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 63
Too low! Try again.
Enter your guess: 69
🎉 Congratulations! You guessed it in 4 attempts.
