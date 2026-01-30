def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
result1 = max_of_three(10, 5, 8)
print(f"Maximum of 10, 5, 8 is: {result1}")

result2 = max_of_three(3, 15, 7)
print(f"Maximum of 3, 15, 7 is: {result2}")

result3 = max_of_three(4, 9, 12)
print(f"Maximum of 4, 9, 12 is: {result3}")