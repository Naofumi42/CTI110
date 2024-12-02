# Kelly Brown
# Date: 11/19/2024
# Assignment Name: P5LAB Self-Checkout Simulation

import random

def addition_quiz():
    """Generates two random numbers for addition and asks the user to solve."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    
    print(f"  {num1}")
    print(f"+ {num2}")
    
    user_answer = int(input("Enter your answer: "))
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

def subtraction_quiz():
    """Generates two random numbers for subtraction and asks the user to solve."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    # Ensure the subtraction result is non-negative
    if num1 < num2:
        num1, num2 = num2, num1
        
    correct_answer = num1 - num2
    
    print(f"  {num1}")
    print(f"- {num2}")
    
    user_answer = int(input("Enter your answer: "))
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

def display_menu():
    """Displays the menu to the user."""
    print("\nMAIN MENU")
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")

def main():
    """Main function to control the program flow."""
    while True:
        display_menu()
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
