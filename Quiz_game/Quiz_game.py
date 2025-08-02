def ask_question(question, options, correct_option, score):
    print(f"\n{question}")
    print("A.", options[0])
    print("B.", options[1])
    print("C.", options[2])
    print("D.", options[3])

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == correct_option:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer was {correct_option}.")

    return score

def main():
    score = 0

    quiz = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "London", "Paris", "Madrid"],
            "correct": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct": "B"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["10", "11", "12", "13"],
            "correct": "C"
        }
    ]

    print("=== Welcome to the Quiz Game ===")

    for q in quiz:
        score = ask_question(q["question"], q["options"], q["correct"], score)

    print(f"\nYour final score is: {score} out of {len(quiz)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
