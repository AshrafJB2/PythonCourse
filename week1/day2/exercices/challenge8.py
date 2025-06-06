data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def ask_questions():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ").strip()
        if user_answer.lower() == item["answer"].lower():
            correct += 1
        else:
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })
    
    return correct, incorrect, wrong_answers

def show_results(correct, incorrect, wrong_answers):
    print(f"\nYou got {correct} correct and {incorrect} incorrect.")

    if wrong_answers:
        print("\nHere are the questions you missed:")
        for item in wrong_answers:
            print(f"- Q: {item['question']}")
            print(f"  Your answer: {item['your_answer']}")
            print(f"  Correct answer: {item['correct_answer']}\n")

    if incorrect > 3:
        print("You got more than 3 wrong answers. Would you like to play again? (yes/no)")
        retry = input().strip().lower()
        if retry == "yes":
            main()

def main():
    print("Welcome to the Star Wars Quiz! \n")
    correct, incorrect, wrong_answers = ask_questions()
    show_results(correct, incorrect, wrong_answers)

main()
