"""
Inheritance in Python

Learn how classes can inherit from other classes.
"""

print("=== BASIC INHERITANCE ===")
# Parent class (Base class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

print("\n=== CALLING PARENT CLASS METHODS ===")
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors
    
    def display_info(self):
        super().display_info()  # Call parent method
        print(f"Doors: {self.doors}")

car = Car("Toyota", "Camry", 4)
car.display_info()

print("\n=== MULTIPLE INHERITANCE ===")
class Flyable:
    def fly(self):
        print("Flying in the sky!")

class Swimmable:
    def swim(self):
        print("Swimming in water!")

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        print(f"{self.name} quacks: Quack!")

duck = Duck("Donald")
duck.speak()
duck.fly()
duck.swim()

print("\n=== METHOD RESOLUTION ORDER (MRO) ===")
print(f"Duck MRO: {Duck.__mro__}")
print(f"Duck MRO (cleaner): {[cls.__name__ for cls in Duck.__mro__]}")

print("\n=== CHECKING INHERITANCE ===")
class Shape:
    pass

class Rectangle(Shape):
    pass

class Square(Rectangle):
    pass

square = Square()

print(f"isinstance(square, Square): {isinstance(square, Square)}")
print(f"isinstance(square, Rectangle): {isinstance(square, Rectangle)}")
print(f"isinstance(square, Shape): {isinstance(square, Shape)}")
print(f"isinstance(square, str): {isinstance(square, str)}")

print(f"\nissubclass(Square, Rectangle): {issubclass(Square, Rectangle)}")
print(f"issubclass(Square, Shape): {issubclass(Square, Shape)}")
print(f"issubclass(Rectangle, Square): {issubclass(Rectangle, Square)}")

print("\n=== OVERRIDING METHODS ===")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.1

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def calculate_bonus(self):
        # Override parent method
        base_bonus = super().calculate_bonus()
        team_bonus = self.team_size * 100
        return base_bonus + team_bonus

employee = Employee("Alice", 50000)
manager = Manager("Bob", 80000, 5)

print(f"{employee.name}'s bonus: ${employee.calculate_bonus()}")
print(f"{manager.name}'s bonus: ${manager.calculate_bonus()}")

print("\n=== ABSTRACT BASE CLASSES ===")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# shape = Shape()  # Error: Can't instantiate abstract class

rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area():.2f}")
print(f"Circle circumference: {circle.perimeter():.2f}")

print("\n=== POLYMORPHISM ===")
# Same method name, different behavior
shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 8)]

for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}")

print("\n=== COMPOSITION OVER INHERITANCE ===")
# Sometimes composition is better than inheritance
class Engine:
    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # Composition: Car HAS-A Engine
    
    def start(self):
        print(f"Starting {self.brand}...")
        self.engine.start()
    
    def stop(self):
        print(f"Stopping {self.brand}...")
        self.engine.stop()

car = Car("Tesla")
car.start()
car.stop()

print("\n=== INHERITANCE BEST PRACTICES ===")
practices = [
    "1. Use inheritance for 'is-a' relationships",
    "2. Use composition for 'has-a' relationships",
    "3. Keep inheritance hierarchies shallow",
    "4. Don't use inheritance just for code reuse",
    "5. Override methods to customize behavior",
    "6. Use super() to call parent class methods",
    "7. Consider abstract base classes for interfaces",
    "8. Be cautious with multiple inheritance"
]

for practice in practices:
    print(practice)

print("\nAll examples executed successfully!")
