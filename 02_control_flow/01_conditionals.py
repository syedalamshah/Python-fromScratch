"""
Conditional Statements in Python

if, elif, and else statements are used for decision making.
"""

print("=== BASIC IF STATEMENT ===")
age = 18
if age >= 18:
    print("You are an adult.")

print("\n=== IF-ELSE STATEMENT ===")
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

print("\n=== IF-ELIF-ELSE STATEMENT ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

print("\n=== NESTED IF STATEMENTS ===")
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")

print("\n=== LOGICAL OPERATORS IN CONDITIONS ===")
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials.")

print("\n=== CHECKING MULTIPLE CONDITIONS ===")
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

print("\n=== TERNARY OPERATOR ===")
# Shorthand if-else
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

print("\n=== CHECKING FOR EMPTY/NONE VALUES ===")
name = ""
if not name:
    print("Name is empty")

items = [1, 2, 3]
if items:
    print("List has items")

value = None
if value is None:
    print("Value is None")

print("\n=== MEMBERSHIP TESTING ===")
fruits = ["apple", "banana", "orange"]
fruit = "banana"

if fruit in fruits:
    print(f"{fruit} is in the list")

number = 5
if 1 <= number <= 10:
    print(f"{number} is between 1 and 10")

print("\nAll examples executed successfully!")
