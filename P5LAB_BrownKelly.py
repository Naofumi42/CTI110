# Kelly Brown
# 2024-11-17
# Assignment Name: P5LAB - Self-Checkout Change Dispenser


import random

# Function to dispense change in coins
def disperse_change(change):
    # Convert change to cents for easier calculation
    cents = round(change * 100)
    
    # Calculate the number of dollars
    dollars = cents // 100
    cents %= 100
    
    # Calculate the number of quarters
    quarters = cents // 25
    cents %= 25
    
    # Calculate the number of dimes
    dimes = cents // 10
    cents %= 10
    
    # Calculate the number of nickels
    nickels = cents // 5
    cents %= 5
    
    # Remaining pennies
    pennies = cents
    
    # Print out the breakdown of coins
    print(f"Change to be returned:")
    if dollars > 0:
        print(f"${dollars} dollar(s)")
    if quarters > 0:
        print(f"{quarters} quarter(s)")
    if dimes > 0:
        print(f"{dimes} dime(s)")
    if nickels > 0:
        print(f"{nickels} nickel(s)")
    if pennies > 0:
        print(f"{pennies} penny(ies)")

# Main function to drive the program
def main():
    # Generate a random total price (customer owes)
    total_owed = round(random.uniform(0.01, 100.00), 2)
    
    # Display the total owed
    print(f"Total amount owed: ${total_owed:.2f}")
    
    # Prompt the user to enter the amount of money they are paying
    cash_given = float(input("Enter the amount of money you are putting into the self-checkout: $"))
    
    # Calculate the amount of change to be returned
    change_owed = round(cash_given - total_owed, 2)
    
    # Check if the user gave enough money
    if change_owed < 0:
        print("Insufficient funds. Please try again.")
    else:
        print(f"Change to be returned: ${change_owed:.2f}")
        # Call the function to disperse the change
        disperse_change(change_owed)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
