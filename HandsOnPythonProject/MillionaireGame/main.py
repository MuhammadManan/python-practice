questions = [
    ["What is the capital of France?", "Paris"],
    ["What is 2 + 2?", "4"],
    ["What is the capital of Spain?", "Madrid"],
    ["What is 5 * 6?", "30"],
    ["What is the capital of Italy?", "Rome"],
    ["What is the largest planet in our solar system?", "Jupiter"], 
    ["What is the boiling point of water in Celsius?", "100"],
    ["What is the chemical symbol for gold?", "Au"],
    ["What is the square root of 16?", "4"],
    ["What is the capital of Japan?", "Tokyo"]
]

def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", answer)

for question, answer in questions:
    ask_question(question, answer)
print("Congratulations! You've completed the quiz.")