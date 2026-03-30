def login_decorator(func):

    def wrapper():
        print("Checking user credentials...")
        func()
        print("Access granted")

    return wrapper


@login_decorator
def login():
    print("User logged in successfully")


login()