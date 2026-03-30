A = 10
def increment_counter(counter):
    return counter + 1

print (f"counter is globally set to: {A}")
counter = increment_counter(A)

print(f"After incrementing, counter is now {counter}")

def increment(counter):
    return counter + 1

final_counter = increment(counter)
print(f"Final counter value is {final_counter}")