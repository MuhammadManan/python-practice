age = int(input("Enter your age: "))  # Convert input to integer
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are an adult.")