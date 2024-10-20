# P3LAB_BrownKelly.py
# Author: Kelly Brown
# Date: 10/20/2024
# Description: This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make a given amount of money.

def main():
    # Prompt the user for input
    money_input = input("Enter a money amount (e.g., 12.34): ")
    
    # Convert the input to cents
    try:
        money = float(money_input)
        cents = int(round(money * 100))
    except ValueError:
        print("Invalid input. Please enter a valid money amount.")
        return

    # Calculate the number of each type of coin
    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    # Output the results
    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

if __name__ == "__main__":
    main()
