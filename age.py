temp = int(input("Enter temperature in Celsius: "))
has_raining = int(input("Is it raining? (1 for Yes, 0 for No): "))

if temp > 40 and has_raining == 1:
    print("It's a hot and rainy day.")