# creating a command line utility for simple file operations by arugments
import argparse

parser = argparse.ArgumentParser(description="Calculator for simple file operations")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")

args = parser.parse_args()
if args.operation == "add":
    print(f"Result: {args.num1 + args.num2}")
elif args.operation == "subtract":
    print(f"Result: {args.num1 - args.num2}")
elif args.operation == "multiply":
    print(f"Result: {args.num1 * args.num2}")
elif args.operation == "divide":
    if args.num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {args.num1 / args.num2}")
else:
    print("Invalid operation. Please choose from add, subtract, multiply, or divide.")