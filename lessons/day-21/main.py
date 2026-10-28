questions = [
    ("What keyword defines a function?", "def"),
    ("What type stores True or False?", "bool"),
]
score = 0
for question, correct_answer in questions:
    answer = input(question + " ")
    if answer.strip().lower() == correct_answer:
        score += 1
print(f"Score: {score}/{len(questions)}")
