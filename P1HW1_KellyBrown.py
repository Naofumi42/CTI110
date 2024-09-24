 # Your Name Kelly Brown
 # Date 09/24/24
 # Assignment Name
 # A brief description of the project

# Function to calculate power
def calculate_power(base, exponent):
    result = base ** exponent
    return result

# Function to perform addition and subtraction
def calculate_sum_and_subtraction(num1, num2, num3):
    sum_result = num1 + num2
    final_result = sum_result - num3
    return final_result

# Get base and exponent from user
base = int(input("Enter the base value: "))
exponent = int(input("Enter the exponent value: "))
power_result = calculate_power(base, exponent)

# Display the power result
print(f"{base} raised to the power of {exponent} is {power_result}!!!")

# Get three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate sum and final result
final_result = calculate_sum_and_subtraction(num1, num2, num3)

# Display the final result
print(f"The result of adding {num1} and {num2}, then subtracting {num3} is {final_result}!!!")
