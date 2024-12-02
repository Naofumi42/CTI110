# Your Name: Kelly Brown
# Date: November 24, 2024
# Assignment Name: P5HW - Math Quiz

import random

# Function to add two random numbers and prompt user for the answer
def addition_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"\nWhat is {num1} + {num2}?")
    
    guess_count = 0
    while True:
        user_answer = int(input("Your answer: "))
        guess_count += 1
        
        if user_answer == correct_answer:
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses:{guess_count} guesses.")
            break
        elif user_answer < correct_answer:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Function to subtract two random numbers and prompt user for the answer
def subtraction_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, num1)  # Ensure num2 is smaller than or equal to num1
    correct_answer = num1 - num2
    print(f"\nWhat is {num1} - {num2}?")
    
    guess_count = 0
    while True:
        user_answer = int(input("Your answer: "))
        guess_count += 1
        
        if user_answer == correct_answer:
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses:{guess_count} guesses.")
            break
        elif user_answer < correct_answer:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Function to display the menu and handle user input
def display_menu():
    print("\nMath Quiz Menu:")
    print("1. Addition Problem")
    print("2. Subtraction Problem")
    print("3. Exit")
    
    choice = input("Please choose one of the menu options: ")
    return choice

def main():
    while True:
        user_choice = display_menu()

        if user_choice == '1':
            addition_problem()
        elif user_choice == '2':
            subtraction_problem()
        elif user_choice == '3':
            print("Thank you for playing!\n Goodbye!!!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

