class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

car1 = Car("Toyota", "Corolla", 2024)
car2 = Car("Honda", "Civic", 2023)

print(type(car1))
print(f"Car 1: {car1.brand} {car1.model} ({car1.year})")
print(type(car2))
print(f"Car 2: {car2.brand} {car2.model} ({car2.year})")