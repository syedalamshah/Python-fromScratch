def save_students_marks(name, marks):
    with open("student.txt", "a") as f:
        f.write(name + "," + str(marks) + "\n")