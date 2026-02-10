# Quiz Application

questions = [
    {
        "question": "What is the output of print(2 + 3)?",
        "options": ["A. 23", "B. 5", "C. 2+3", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store text?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "C"
    }
]

score = 0

print("📝 Welcome to Python Quiz 📝\n")

for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!\n")

print("🎉 Quiz Completed!")
print(f"Your Score: {score} / {len(questions)}")
