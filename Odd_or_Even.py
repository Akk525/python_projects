# Get user input for the number to be checked.
number = int(input("Which number do you want to check? "))

# Check if the number is even by dividing it by 2 and checking if the remainder is 0.
if number % 2 == 0:
    # If the remainder is 0, then the number is even.
    print("This is an even number.")
else:
    # If the remainder is not 0, then the number is odd.
    print("This is an odd number.")
