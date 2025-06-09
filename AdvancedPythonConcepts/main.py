def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello() # syntax sugar for say_hello = decorator(say_hello)
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
# Decorators are a way to modify or enhance functions or methods without changing their code.