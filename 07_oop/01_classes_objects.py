"""
Object-Oriented Programming (OOP) in Python - Classes and Objects

Learn how to create and use classes and objects.
"""

print("=== BASIC CLASS ===")
# Define a class
class Dog:
    def bark(self):
        print("Woof!")

# Create an object (instance)
my_dog = Dog()
my_dog.bark()

print("\n=== CLASS WITH CONSTRUCTOR ===")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.introduce()
person2.introduce()

print("\n=== CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES ===")
class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"{self.brand} {self.model} has {self.wheels} wheels")

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.display_info()
car2.display_info()

print(f"Class attribute accessed via class: {Car.wheels}")
print(f"Class attribute accessed via instance: {car1.wheels}")

print("\n=== METHODS ===")
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

calc = Calculator()
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")
print(f"10 × 5 = {calc.multiply(10, 5)}")
print(f"10 ÷ 5 = {calc.divide(10, 5)}")

print("\n=== ENCAPSULATION (PRIVATE ATTRIBUTES) ===")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")
# print(account.__balance)  # This would raise AttributeError

print("\n=== STRING REPRESENTATION ===")
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        # User-friendly string representation
        return f"'{self.title}' by {self.author} ({self.year})"
    
    def __repr__(self):
        # Developer-friendly representation
        return f"Book('{self.title}', '{self.author}', {self.year})"

book = Book("1984", "George Orwell", 1949)
print(f"str(book): {str(book)}")
print(f"repr(book): {repr(book)}")

print("\n=== CLASS METHODS ===")
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp1 = Temperature(25)
print(f"{temp1.celsius}°C = {temp1.to_fahrenheit()}°F")

temp2 = Temperature.from_fahrenheit(77)
print(f"77°F = {temp2.celsius:.1f}°C")

print("\n=== STATIC METHODS ===")
class MathOperations:
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

print(f"Is 10 even? {MathOperations.is_even(10)}")
print(f"Is 7 prime? {MathOperations.is_prime(7)}")

print("\n=== PROPERTY DECORATOR ===")
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

circle.radius = 10
print(f"New radius: {circle.radius}")
print(f"New area: {circle.area:.2f}")

print("\n=== OBJECT COMPARISON ===")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")

print("\nAll examples executed successfully!")
