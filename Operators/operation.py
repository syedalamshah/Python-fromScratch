num1 = int(input("Enter first number: "))
num2= int (input("Enter second number: "))

substraction = num1 - num2
addition = num1 + num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

if(num1 > num2):
    print("num1 is greater than num2")
elif (num1 < num2):
    print("num2 is greater than num1")
else:
    print("num1 is equal to num2")


print("substraction:",substraction)
print("addition",addition  )
print("multiplication:",multiplication)
print("division:",division)
print("modulus:",modulus)