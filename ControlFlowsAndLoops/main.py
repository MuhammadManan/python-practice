'''
age = int(input("Enter your age: "))  # Convert input to integer
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are an adult.")

'''

# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")

# i = 1
# while i <= 10:
#     print(f"5 x {i} = {5 * i}")
#     i += 1

c = 32

match c:
    case 1:
        print("c is 1")
    case 2:
        print("c is 2")
    case 3:
        print("c is 3")    
    case _:
        print("c is something else")