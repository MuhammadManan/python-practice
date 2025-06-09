name = "longwordlessthan10characters"

score = 0

print("String for tough quiz:", name)
print("Let's test your advanced knowledge of string indexing and slicing!\n")

# Question 1: What is the 3rd character from the end?
ans = input("1. What is name[-3]? ")
if ans == name[-3]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[-3]}'.")

# Question 2: What is the substring from index 5 to the second last character?
ans = input("2. What is name[5:-1]? ")
if ans == name[5:-1]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[5:-1]}'.")

# Question 3: What is every second character from index 2 to 12?
ans = input("3. What is name[2:13:2]? ")
if ans == name[2:13:2]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[2:13:2]}'.")

# Question 4: What is the reversed string?
ans = input("4. What is name[::-1]? ")
if ans == name[::-1]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[::-1]}'.")

# Question 5: What is the substring from index 0 to 20 with a step of 3?
ans = input("5. What is name[0:21:3]? ")
if ans == name[0:21:3]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[0:21:3]}'.")

print(f"\nTough quiz finished! Your score: {score}/5")