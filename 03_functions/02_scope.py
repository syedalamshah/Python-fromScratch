"""
Function Scope and Global Variables

Understanding variable scope in Python.
"""

print("=== LOCAL SCOPE ===")
def my_function():
    local_var = "I'm local"
    print(f"Inside function: {local_var}")

my_function()
# print(local_var)  # This would cause an error - local_var is not accessible here

print("\n=== GLOBAL SCOPE ===")
global_var = "I'm global"

def access_global():
    print(f"Inside function: {global_var}")

access_global()
print(f"Outside function: {global_var}")

print("\n=== MODIFYING GLOBAL VARIABLES ===")
counter = 0

def increment():
    global counter  # Must use 'global' keyword to modify
    counter += 1
    print(f"Counter inside function: {counter}")

increment()
increment()
print(f"Counter outside function: {counter}")

print("\n=== NONLOCAL KEYWORD (NESTED FUNCTIONS) ===")
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # Refers to x in outer function
        x = "modified by inner"
        print(f"Inner function: x = {x}")
    
    print(f"Before inner: x = {x}")
    inner()
    print(f"After inner: x = {x}")

outer()

print("\n=== SCOPE RESOLUTION (LEGB RULE) ===")
# LEGB: Local -> Enclosing -> Global -> Built-in
x = "global x"

def outer_func():
    x = "outer x"
    
    def inner_func():
        x = "inner x"
        print(f"Inner: {x}")
    
    inner_func()
    print(f"Outer: {x}")

outer_func()
print(f"Global: {x}")

print("\n=== BEST PRACTICES ===")
# Prefer passing parameters and returning values over using global
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Result: {result}")

# Avoid globals when possible
total = 0

def better_increment(current_value):
    return current_value + 1

total = better_increment(total)
total = better_increment(total)
print(f"Total: {total}")

print("\nAll examples executed successfully!")
