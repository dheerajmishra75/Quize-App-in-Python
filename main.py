def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": "C) Paris"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Jupiter", "Mars", "Saturn"],
            "answer": "B) Jupiter" 
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "A) H2O"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
            "answer": "A) William Shakespeare"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "D) Pacific Ocean"
        }
    ]

    score = 0
    for index, q in enumerate(questions):
        print(f"Q{index + 1}: {q['question']}")

        letters = ["A", "B", "C", "D"]

        for i, option in enumerate(q['options']):
            print(f"{letters[i]}) {option}")

        user_answer = input("Your answer (A/B/C/D): ")

        if user_answer.strip().upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")

    print(f"Your final score is: {score}/{len(questions)}")


run_quiz()