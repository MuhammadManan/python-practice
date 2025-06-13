try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    match operation:
        case '+':
            print(f"The result of {a} + {b} is: {a + b}")
        case '-':
            print(f"The result of {a} - {b} is: {a - b}")
        case '*':
            print(f"The result of {a} * {b} is: {a * b}")
        case '/':
            if b != 0:
                print(f"The result of {a} / {b} is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Error: Invalid operation.")
except Exception as e:
    print(f"An error occurred: {e}")