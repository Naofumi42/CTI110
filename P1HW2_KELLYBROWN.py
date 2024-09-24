# Your Name Kelly Brown  
# Date 09/24/24
# Assignment Name: Travel Budget Calculator
# A brief description of the project: This program helps users manage their travel budget by calculating total expenses based on user inputs.

# Step 1: Ask user to enter their budget
budget = float(input("Enter your travel budget: $"))

# Step 2: Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Step 3: Ask user for amount they will spend on gas
gas_expense = float(input("Enter amount you will spend on gas: $"))

# Step 4: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter amount you will spend on accommodation: $"))

# Step 5: Ask user for amount they will spend on food
food_expense = float(input("Enter amount you will spend on food: $"))

# Step 6: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 7: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 8: Display results
print(f"\nTravel to {destination}:")
print(f"Total expenses: ${total_expenses:.2f}")
print(f"Remaining budget: ${remaining_budget:.2f}")

# Step 9: Provide a message based on the remaining budget
if remaining_budget >= 0:
    print("You are within your budget. Enjoy your trip!")
else:
    print("You are over budget. Consider reducing your expenses.")
