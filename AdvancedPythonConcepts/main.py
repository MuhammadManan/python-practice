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


'''class Employee:
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
e.get_company()'''
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

'''class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee name: {self.name}, Salary: {self.salary}"
    
    def __repr__(self):
        return f"Employee({self.name}, {self.salary})"
    
    def __len__(self):
        return len(self.name)
    
e1 = Employee("Manan", 70000)
print(str(e1))
print(repr(e1))
print(len(e1))  # Output: 5 (length of the name "Manan")'''

# Exception Handling & Custom Errors Quiz
'''
score = 0

print("Python Exception Handling & Custom Errors Quiz\n")

# 1
ans = input("1. What keyword is used to handle exceptions in Python? ")
if ans.strip().lower() == "try":
    score += 1

# 2
ans = input("2. What keyword is used to catch exceptions? ")
if ans.strip().lower() == "except":
    score += 1

# 3
ans = input("3. What keyword is used to execute code after try/except, regardless of exceptions? ")
if ans.strip().lower() == "finally":
    score += 1

# 4
ans = input("4. What keyword is used to raise an exception manually? ")
if ans.strip().lower() == "raise":
    score += 1

# 5
ans = input("5. What is the output?\ntry:\n    1/0\nexcept ZeroDivisionError:\n    print('Error')\n")
if ans.strip().lower() == "error":
    score += 1

# 6
ans = input("6. What exception is raised by int('abc')? ")
if ans.strip().lower() == "valueerror":
    score += 1

# 7
ans = input("7. What exception is raised by open('nofile.txt') if the file does not exist? ")
if ans.strip().lower() == "file not found error" or ans.strip().lower() == "filenotfounderror":
    score += 1

# 8
ans = input("8. What is the base class for all exceptions in Python? ")
if ans.strip().lower() == "exception":
    score += 1

# 9
ans = input("9. What is the output?\ntry:\n    print(1)\nfinally:\n    print(2)\n")
if ans.replace(" ", "") == "1\n2" or ans.replace(" ", "") == "1 2":
    score += 1

# 10
ans = input("10. What does 'pass' do in an except block? ")
if "nothing" in ans.lower() or "no operation" in ans.lower():
    score += 1

# 11
ans = input("11. How do you define a custom exception class called MyError? (Just the class header) ")
if "class myerror" in ans.lower():
    score += 1

# 12
ans = input("12. What is the output?\ntry:\n    raise ValueError('Oops!')\nexcept ValueError as e:\n    print(e)\n")
if "oops" in ans.lower():
    score += 1

# 13
ans = input("13. What exception is raised by [1,2,3][5]? ")
if ans.strip().lower() == "indexerror":
    score += 1

# 14
ans = input("14. What exception is raised by {}['a']? ")
if ans.strip().lower() == "keyerror":
    score += 1

# 15
ans = input("15. What is the output?\ntry:\n    print(1/1)\nexcept ZeroDivisionError:\n    print('zero')\nelse:\n    print('done')\n")
if ans.replace(" ", "") == "1.0\ndone" or ans.replace(" ", "") == "1.0 done":
    score += 1

# 16
ans = input("16. What is the purpose of the 'else' block in try/except/else? ")
if "no exception" in ans.lower() or "if no exception" in ans.lower():
    score += 1

# 17
ans = input("17. What is the output?\ntry:\n    raise Exception('fail')\nexcept Exception as e:\n    print(type(e).__name__)\n")
if ans.strip().lower() == "exception":
    score += 1

# 18
ans = input("18. What exception is raised by int('')? ")
if ans.strip().lower() == "valueerror":
    score += 1

# 19
ans = input("19. What exception is raised by import math, then math.sqrt(-1)? ")
if ans.strip().lower() == "valueerror":
    score += 1

# 20
ans = input("20. Fill in the blank: To create a custom exception, inherit from the ______ class. ")
if ans.strip().lower() == "exception":
    score += 1

print(f"\nQuiz finished! Your score: {score}/20")'''

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num2 == 0:
    print("Error: Division by zero is not allowed.")
    raise ValueError("Division by zero is not allowed.")
    num3 = num1 / num2



