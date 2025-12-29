"""
Practice Exercises - Advanced

More challenging exercises to test your Python skills!
"""

print("=" * 60)
print("PYTHON ADVANCED - PRACTICE EXERCISES")
print("=" * 60)

# Exercise 1: Temperature Converter
print("\n--- Exercise 1: Temperature Converter ---")
print("Create a function that converts Celsius to Fahrenheit")
print("Formula: F = (C × 9/5) + 32")
print("Test with: 0°C, 25°C, 100°C")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# temps = [0, 25, 100]
# for temp in temps:
#     fahrenheit = celsius_to_fahrenheit(temp)
#     print(f"{temp}°C = {fahrenheit}°F")

# Exercise 2: Palindrome Checker
print("\n--- Exercise 2: Palindrome Checker ---")
print("Create a function that checks if a string is a palindrome")
print("(reads the same forwards and backwards)")
print("Test with: 'radar', 'hello', 'level'")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def is_palindrome(text):
#     text = text.lower()
#     return text == text[::-1]
#
# words = ['radar', 'hello', 'level']
# for word in words:
#     result = is_palindrome(word)
#     print(f"'{word}' is palindrome: {result}")

# Exercise 3: Count Vowels
print("\n--- Exercise 3: Count Vowels ---")
print("Create a function that counts vowels in a string")
print("Test with: 'Python Programming'")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def count_vowels(text):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
#
# text = "Python Programming"
# print(f"Vowels in '{text}': {count_vowels(text)}")

# Exercise 4: List Statistics
print("\n--- Exercise 4: List Statistics ---")
print("Create a function that returns min, max, and average of a list")
print("Test with: [10, 20, 30, 40, 50]")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def list_stats(numbers):
#     return {
#         'min': min(numbers),
#         'max': max(numbers),
#         'average': sum(numbers) / len(numbers)
#     }
#
# nums = [10, 20, 30, 40, 50]
# stats = list_stats(nums)
# print(f"Numbers: {nums}")
# print(f"Stats: {stats}")

# Exercise 5: Fibonacci Sequence
print("\n--- Exercise 5: Fibonacci Sequence ---")
print("Generate first 10 Fibonacci numbers")
print("(Each number is sum of previous two: 0, 1, 1, 2, 3, 5, ...)")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib
#
# result = fibonacci(10)
# print(f"First 10 Fibonacci numbers: {result}")

# Exercise 6: Remove Duplicates
print("\n--- Exercise 6: Remove Duplicates ---")
print("Remove duplicates from a list while preserving order")
print("Test with: [1, 2, 2, 3, 4, 4, 4, 5]")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def remove_duplicates(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result
#
# numbers = [1, 2, 2, 3, 4, 4, 4, 5]
# print(f"Original: {numbers}")
# print(f"Without duplicates: {remove_duplicates(numbers)}")

# Exercise 7: Word Frequency
print("\n--- Exercise 7: Word Frequency ---")
print("Count frequency of each word in a sentence")
print("Test with: 'hello world hello python world'")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def word_frequency(sentence):
#     words = sentence.split()
#     frequency = {}
#     for word in words:
#         frequency[word] = frequency.get(word, 0) + 1
#     return frequency
#
# sentence = "hello world hello python world"
# freq = word_frequency(sentence)
# print(f"Word frequency: {freq}")

# Exercise 8: Prime Numbers
print("\n--- Exercise 8: Prime Numbers ---")
print("Find all prime numbers up to 30")
print("(A prime number is divisible only by 1 and itself)")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# primes = [n for n in range(2, 31) if is_prime(n)]
# print(f"Prime numbers up to 30: {primes}")

# Exercise 9: Student Grade System
print("\n--- Exercise 9: Student Grade System ---")
print("Create a class Student with:")
print("- name and scores attributes")
print("- method to calculate average")
print("- method to get letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores
#     
#     def average(self):
#         return sum(self.scores) / len(self.scores)
#     
#     def letter_grade(self):
#         avg = self.average()
#         if avg >= 90: return 'A'
#         elif avg >= 80: return 'B'
#         elif avg >= 70: return 'C'
#         elif avg >= 60: return 'D'
#         else: return 'F'
#
# student = Student("Alice", [85, 92, 88, 90])
# print(f"{student.name}'s average: {student.average():.1f}")
# print(f"Grade: {student.letter_grade()}")

# Exercise 10: Challenge - Number Guessing Game
print("\n--- Exercise 10: Challenge - Number Guessing Game ---")
print("Create a simple number guessing game:")
print("- Computer picks a random number between 1-100")
print("- Player has 7 attempts to guess")
print("- Give 'higher' or 'lower' hints")
print("Note: This requires input(), so it's better run interactively")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# import random
#
# def guessing_game():
#     number = random.randint(1, 100)
#     attempts = 7
#     
#     print("I'm thinking of a number between 1 and 100")
#     print(f"You have {attempts} attempts")
#     
#     for i in range(attempts):
#         guess = int(input(f"Attempt {i+1}: Enter your guess: "))
#         
#         if guess == number:
#             print(f"Congratulations! You got it in {i+1} attempts!")
#             return
#         elif guess < number:
#             print("Higher!")
#         else:
#             print("Lower!")
#     
#     print(f"Sorry! The number was {number}")
#
# # Uncomment to play (requires interactive mode):
# # guessing_game()

print("\n" + "=" * 60)
print("TIPS:")
print("- These exercises are more challenging!")
print("- Break down complex problems into smaller steps")
print("- Test your functions with different inputs")
print("- Don't peek at solutions until you've tried!")
print("=" * 60)

print("\nAll exercises loaded successfully!")
print("Uncomment the example solutions to run them.")
