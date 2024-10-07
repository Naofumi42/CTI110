# Kelly Brown
# 10/05/24
# Assignment Name: P2LAB2
# A brief description of the project: This program creates a dictionary of vehicles and their MPG,
# allows the user to select a vehicle, and calculates the gas needed for a specified distance.

# Create the dictionary of vehicles and their MPG
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all the keys from the dictionary
keys = vehicles.keys()

# Print the keys
print("Available vehicles:", keys)

# Prompt the user to enter a vehicle
selected_vehicle = input("Enter one of the vehicles from the list: ")

# Get and display the MPG for the selected vehicle
if selected_vehicle in vehicles:
    mpg = vehicles[selected_vehicle]
    print(f"The MPG for {selected_vehicle} is {mpg}")

    # Prompt the user for the number of miles to drive
    miles = float(input("Enter the number of miles you will drive: "))

    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg

    # Display the result
    print(f"To drive a {selected_vehicle} {miles:.2f} miles, you will need {gallons_needed:.2f} gallons of gas.")
else:
    print("Invalid vehicle selection. Please run the program again and choose from the available vehicles.")
