class Student:

    def __init__ (self, name ,marks) :
        self.name = name
        self.marks = marks
student1 = Student("Alice", 85)
student2 = Student("Bob", 90)
print(type(student1))
print(f"Student 1: {student1.name} with marks {student1.marks}")
print(type(student2))
print(f"Student 2: {student2.name} with marks {student2.marks}")