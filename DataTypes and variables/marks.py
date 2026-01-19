marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

if marks >= 75 and attendance > 85:
    print("You are eligible for the scholarship.")
else:
    print("You are not eligible for the scholarship.")