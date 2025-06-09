'''class Employee:

    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond

    def info(self):
        print(self)
        print(f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond}")

e = Employee("John Doe", 50000, 2)
e.info()
'''

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y  

    def __add__(self, other):
        return point((self.x + other.x) , (self.y + other.y))
    
    def show(self):
        print(f"Point({self.x}, {self.y})")

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    
p1 = point(10, 20)
# print(p1)
p2 = point(30, 40)
# print(p2)
p3 = p1 + p2
p3.show()  # This will print the result of the addition in a readable format
p3.__str__()  # This will return the string representation of p3

print(type(p3))