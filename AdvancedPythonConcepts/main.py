'''def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello() '''# syntax sugar for say_hello = decorator(say_hello)
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
# Decorators are a way to modify or enhance functions or methods without changing their code.

def repeat(n):
    def decorator(func):
        def wrapper(arg):
            for i in range(n):
                func(arg)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Manan!")  # Output: Hello, Manan! (3 times)

# greet("Alice")  # Output: Hello, Alice! (3 times)

# print('beofre decorator')
# dec = repeat(3)
# print('after decorator')
# print('before wrapping')
# wrp = dec(greet)
# print('after wrapping')
# print('before calling')
# wrp("Alice")  # Output: Hello, Alice! (3 times)
# print('after calling')
