# Kelly Brown
# 10/26/2024
# Assignment Name
# A brief description of the project

# This program calculates the gross pay for an employee based on their worked hours,
# pay rate, and whether they worked overtime.

# Get employee details from user input
employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Determine if there are overtime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
else:
    overtime_hours = 0

# Calculate regular hours and pay
regular_hours = hours_worked - overtime_hours
regular_pay = regular_hours * pay_rate

# Calculate overtime pay
overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print(f"Employee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked:.2f}")
print(f"Overtime Hours: {overtime_hours:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Pay for Regular Hours: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
