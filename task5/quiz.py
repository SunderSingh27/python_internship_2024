# Quiz Game

# Load Quiz Questions
quiz_questions = {
    "What is the capital of France?": {
        "A": "Berlin",
        "B": "Paris",
        "C": "London",
        "D": "Rome",
        "correct": "B"
    },
    "Who painted the Mona Lisa?": {
        "A": "Leonardo da Vinci",
        "B": "Michelangelo",
        "C": "Raphael",
        "D": "Caravaggio",
        "correct": "A"
    },
    "What is the largest planet in our solar system?": {
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Uranus",
        "correct": "C"
    }
}

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Rules: Choose the correct answer from the options.")

def present_quiz_questions():
    score = 0
    for question, options in quiz_questions.items():
        print(question)
        for option, value in options.items():
            if option != "correct":
                print(f"{option}: {value}")
        answer = input("Choose your answer: ")
        if answer.upper() == options["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {options['correct']}: {options[options['correct']]}")
    return score

def calculate_final_score(score):
    total_questions = len(quiz_questions)
    percentage = (score / total_questions) * 100
    if percentage >= 80:
        performance_message = "Excellent!"
    elif percentage >= 60:
        performance_message = "Good!"
    else:
        performance_message = "Needs improvement."
    return percentage, performance_message

def display_final_results(score, percentage, performance_message):
    print(f"Your final score is {score} out of {len(quiz_questions)}.")
    print(f"Your percentage is {percentage:.2f}%.")
    print(performance_message)

def play_again():
    play_again_input = input("Do you want to play again? (yes/no): ")
    if play_again_input.lower() == "yes":
        return True
    else:
        return False

def main():
    display_welcome_message()
    while True:
        score = present_quiz_questions()
        percentage, performance_message = calculate_final_score(score)
        display_final_results(score, percentage, performance_message)
        if not play_again():
            break

if __name__ == "__main__":
    main()