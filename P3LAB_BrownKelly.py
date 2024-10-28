# P3LAB_BrownKelly.py
# Author: Kelly Brown   
# Date: 10/20/2024
# Description: This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make a given amount of money.

def main():
    # Prompt user for money input
    money_input = float(input("Enter an amount of money (e.g., 12.34): "))
    
    # Check if the input is zero
    if money_input == 0:
        print("No Change.")
                    
    # Convert money to cents
    total_cents = int(money_input * 100)
    
    # Calculate number of dollars
    dollars = total_cents // 100
    total_cents %= 100
    
    # Calculate number of quarters
    quarters = total_cents // 25
    total_cents %= 25
    
    # Calculate number of dimes
    dimes = total_cents // 10
    total_cents %= 10
    
    # Calculate number of nickels
    nickels = total_cents // 5
    total_cents %= 5
    
    # Remaining cents are pennies
    pennies = total_cents
    
    # Display the results
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

# Call the main function to execute the program
if __name__ == "__main__":
    main()
