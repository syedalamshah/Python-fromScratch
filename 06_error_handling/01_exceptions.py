"""
Error Handling in Python

Learn how to handle errors and exceptions gracefully.
"""

print("=== BASIC TRY-EXCEPT ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("\n=== HANDLING MULTIPLE EXCEPTIONS ===")
try:
    # This will cause TypeError
    result = "10" + 5
except ZeroDivisionError:
    print("Division by zero error")
except TypeError:
    print("Type error: Cannot add string and integer")

print("\n=== CATCHING MULTIPLE EXCEPTION TYPES ===")
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error occurred: {e}")

print("\n=== GENERIC EXCEPTION HANDLER ===")
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {type(e).__name__}: {e}")

print("\n=== TRY-EXCEPT-ELSE ===")
# else block runs if no exception occurs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Division successful: {result}")

print("\n=== TRY-EXCEPT-FINALLY ===")
# finally block always executes
try:
    file = open("/tmp/test_file.txt", "w")
    file.write("Hello, World!")
except IOError:
    print("File error occurred")
finally:
    print("Cleanup: Closing file...")
    try:
        file.close()
    except:
        pass

print("\n=== COMPLETE TRY-EXCEPT-ELSE-FINALLY ===")
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed")

divide(10, 2)
print()
divide(10, 0)

print("\n=== RAISING EXCEPTIONS ===")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

print("\n=== CUSTOM EXCEPTIONS ===")
class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses"""
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain @")
    if "." not in email:
        raise InvalidEmailError("Email must contain a domain")
    return True

try:
    validate_email("invalid-email")
except InvalidEmailError as e:
    print(f"Email validation failed: {e}")

print("\n=== COMMON BUILT-IN EXCEPTIONS ===")
exceptions = {
    "ZeroDivisionError": "Division by zero",
    "ValueError": "Invalid value for operation",
    "TypeError": "Invalid type for operation",
    "IndexError": "List index out of range",
    "KeyError": "Dictionary key not found",
    "FileNotFoundError": "File doesn't exist",
    "AttributeError": "Object has no attribute",
    "ImportError": "Module import failed",
    "NameError": "Variable not defined",
    "KeyboardInterrupt": "User interrupted execution"
}

for exc, desc in exceptions.items():
    print(f"{exc:20} - {desc}")

print("\n=== EXCEPTION EXAMPLES ===")

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("IndexError: List index out of range")

# KeyError
try:
    d = {"a": 1, "b": 2}
    print(d["c"])
except KeyError:
    print("KeyError: Key not found in dictionary")

# ValueError
try:
    num = int("not a number")
except ValueError:
    print("ValueError: Cannot convert string to integer")

# FileNotFoundError
try:
    with open("/nonexistent/file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("FileNotFoundError: File does not exist")

print("\n=== ASSERTING CONDITIONS ===")
# assert raises AssertionError if condition is False
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")

avg = calculate_average([1, 2, 3, 4, 5])
print(f"Average: {avg}")

print("\n=== NESTED EXCEPTION HANDLING ===")
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner: Caught division by zero")
        raise  # Re-raise the exception
except ZeroDivisionError:
    print("Outer: Caught re-raised exception")

print("\n=== EXCEPTION INFORMATION ===")
import traceback

try:
    x = 1 / 0
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {str(e)}")
    print(f"Exception args: {e.args}")
    print("\nTraceback:")
    traceback.print_exc()

print("\n=== BEST PRACTICES ===")
print("1. Catch specific exceptions, not generic Exception")
print("2. Don't use bare 'except:' clause")
print("3. Use finally for cleanup (close files, connections)")
print("4. Don't suppress exceptions silently")
print("5. Raise exceptions for exceptional conditions")
print("6. Use custom exceptions for domain-specific errors")
print("7. Log exceptions for debugging")

print("\n=== CONTEXT MANAGERS (WITH STATEMENT) ===")
# Automatically handles exceptions and cleanup
print("With statement handles file closing automatically:")
try:
    with open("/tmp/example.txt", "w") as f:
        f.write("Hello, World!")
    print("File written and closed automatically")
except Exception as e:
    print(f"Error: {e}")

print("\nAll examples executed successfully!")
