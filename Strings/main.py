'''name = "Monika"
print(name[0])
print(name[5])
# print(name[6])
print(name[-6])
# print(name[-7]) # out of range error'''

name = "longwordlessthan10characters"

score = 0

print("String for quiz:", name)
print("Let's test your knowledge of string indexing and slicing!\n")

# Question 1: Positive Indexing
ans = input("1. What is name[4]? ")
if ans == name[4]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[4]}'.")

# Question 2: Negative Indexing
ans = input("2. What is name[-1]? ")
if ans == name[-1]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[-1]}'.")

# Question 3: Positive Slicing
ans = input("3. What is name[2:7]? ")
if ans == name[2:7]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[2:7]}'.")

# Question 4: Negative Slicing
ans = input("4. What is name[-5:-1]? ")
if ans == name[-5:-1]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[-5:-1]}'.")

# Question 5: Full Slice
ans = input("5. What is name[:] (the whole string)? ")
if ans == name[:]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is '{name[:]}'.")

print(f"\nQuiz finished! Your score: {score}/5")