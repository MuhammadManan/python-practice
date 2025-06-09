class Employee:

    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond

    def info(self):
        print(self)
        print(f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond}")

e = Employee("John Doe", 50000, 2)
e.info()
