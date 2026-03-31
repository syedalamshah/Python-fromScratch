try:
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter a second number: "))  # This line will raise a ValueError if the input is not a valid integer
    print("The number you entered is:", first_number)
    print("The second number you entered is:", second_number)
    result = first_number / second_number  # This line will raise a ZeroDivisionError if second_number is zero
    print("The result of the division is:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")