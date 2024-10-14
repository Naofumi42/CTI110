# Kelly Brown   
# 10/13/2024
# P2HW2 - Grade Calculator
# This program calculates various statistics for a list of grades

# Pseudocode:
# 1. Initialize an empty list to store grades
# 2. For each module 1 through 6:
#    a. Prompt user to enter grade for the module
#    b. Convert input to float
#    c. Append grade to the list
# 3. Calculate and store:
#    a. Lowest grade (min of list)
#    b. Highest grade (max of list)
#    c. Sum of grades (sum of list)
#    d. Average of grades (sum / length of list)
# 4. Display results formatted as specified

# Initialize empty list to store grades
grades = []

# Input grades for each module
for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades.append(grade)

# Calculate statistics
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade}")
print(f"Highest Grade:     {highest_grade}")
print(f"Sum of Grades:     {sum_of_grades}")
print(f"Average:           {average:.2f}")
print("---------------------------------")
