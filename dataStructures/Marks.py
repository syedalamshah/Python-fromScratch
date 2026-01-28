fruits = ["apple", "banana", "cherry"]
vegetables = ["broccoli", "spinach", "kale"]
grains = ["rice", "wheat", "oats"]

print("Fruits:", fruits)
print("Vegetables:", vegetables)
print("Grains:", grains)

vegetables.append("lettuce")
print("Updated Vegetables:", vegetables)

grains.remove("wheat")
print("Updated Grains:", grains)

appended_fruits = fruits + ["orange", "grape"]
print("Appended Fruits:", appended_fruits)
all_foods = fruits + vegetables + grains    