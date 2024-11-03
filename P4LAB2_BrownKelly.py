def display_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        user_input = input("Enter an integer (zero or higher): ")
        try:
            number = int(user_input)

            if number < 0:
                print("This Program does not handle negative values.")
            else:
                display_multiplication_table(number)

        except ValueError:
            print("Please enter a valid integer.")

        run_again = input("Do you wish to run the program again? (yes/no): ").strip().lower()
        if run_again != 'yes':
            break

# Run the program
main()
