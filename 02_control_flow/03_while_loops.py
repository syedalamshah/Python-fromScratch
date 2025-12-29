"""
While Loops in Python

While loops execute as long as a condition is true.
"""

print("=== BASIC WHILE LOOP ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print("\n=== WHILE LOOP WITH CONDITION ===")
number = 1
while number <= 10:
    print(number, end=" ")
    number += 2
print("\nOdd numbers from 1 to 10")

print("\n=== WHILE LOOP WITH BREAK ===")
i = 0
while True:  # Infinite loop
    if i >= 5:
        break
    print(i, end=" ")
    i += 1
print("\nBroke out of infinite loop")

print("\n=== WHILE LOOP WITH CONTINUE ===")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num, end=" ")
print("\nOdd numbers (using continue)")

print("\n=== WHILE LOOP WITH ELSE ===")
# else executes when condition becomes false
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
else:
    print("While loop completed normally")

print("\n=== USER INPUT SIMULATION (commented) ===")
# Example of input validation with while loop
# Uncomment to try interactively:
# while True:
#     age = input("Enter your age (0 to quit): ")
#     age = int(age)
#     if age == 0:
#         break
#     if age < 0:
#         print("Age cannot be negative!")
#         continue
#     print(f"Your age is {age}")

print("# Common pattern: while True with break for input validation")

print("\n=== COUNTDOWN EXAMPLE ===")
countdown = 5
while countdown > 0:
    print(f"{countdown}...", end=" ")
    countdown -= 1
print("Blast off!")

print("\n=== WHILE VS FOR ===")
print("Use for loops when you know the number of iterations")
print("Use while loops when you don't know how many iterations needed")

# For loop example
print("\nFor loop (known iterations):")
for i in range(3):
    print(f"Iteration {i}")

# While loop example (unknown iterations - would continue until condition met)
print("\nWhile loop (condition-based):")
value = 1
while value < 8:
    print(f"Value: {value}")
    value *= 2

print("\n=== NESTED WHILE LOOPS ===")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1

print("\nAll examples executed successfully!")
