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
'''
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

greet("Manan!")  # Output: Hello, Manan! (3 times)'''

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


class Employee:
    company = "TechCorp"  # Class variable shared by all instances

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
    
    @property
    def first_name(self):
          fname = self.name.split(" ")[0]
          print(fname)
          return fname
    
    @first_name.setter
    def first_name(self, fname):
         self.name = f"{fname} {self.name.split(" ")[1]}"
        #  print(self.name)

    @property
    def fullname(self):
         return self.name
    
    @staticmethod
    def sum(a,b):
        print(a + b)

    @classmethod
    def get_company(cls):
        print(f"Company: {cls.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e = Employee("Manan Azhar", 70000)
Employee.get_company()
e.change_company("NewTech")
e.get_company()
# print(e.name)
# print(e.salary)

'''e.first_name()
e.set_first_name("Hanan")
print(e.name)'''

'''print(e.name)
e.first_name = "John"
print(e.fullname)
print(e.name)'''


# e.sum(5, 10)  # Output: 15
# Employee.sum(33, 44)  # Output: 77