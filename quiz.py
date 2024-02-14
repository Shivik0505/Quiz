import random


def load_quiz_questions():
    # Define a list of quiz questions and their corresponding answers
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["a. London", "b. Paris", "c. Rome", "d. Madrid"],
            "answer": "b"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["a. Mars", "b. Jupiter", "c. Venus", "d. Saturn"],
            "answer": "b"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": ["a. Leonardo da Vinci", "b. Vincent van Gogh", "c. Pablo Picasso", "d. Michelangelo"],
            "answer": "a"
        },
        {
            "question": "What is the capital of India?",
            "choices": ["a. New Delhi", "b. Mumbai", "c. Nagpur", "d. Pune"],
            "answer": "a"
        },
        {
            "question": "Who is the Prime Minister of India?",
            "choices": ["a. Rahul Gandhi", "b. Narendra Modi", "c. Mikhail Mishustin", "d. Joe Biden"],
            "answer": "b"
        },
        {
            "question": "What is the world's fastest bird?",
            "choices": ["a. Eurasian Hobby", "b. Peregrine Falcon", "c. Common Swift", "d. Gyrfalcon"],
            "answer": "b"
        },
    ]

    return quiz_questions


def calculate_final_score(score, total_questions):
    # Calculate the final score as a percentage
    final_score = (score / total_questions) * 100
    return final_score


def display_final_results(final_score):
    # Display the final score to the user
    print("Quiz Completed!")
    print(f"Your Final Score: {final_score}%")


def present_quiz_questions(quiz_questions):
    # Shuffle the quiz questions to make it more challenging
    random.shuffle(quiz_questions)

    # Initialize the score and question counter
    score = 0
    question_counter = 1

    # Iterate through each quiz question
    for question in quiz_questions:
        print(f"\nQuestion {question_counter}:")
        print(question["question"])
        for choice in question["choices"]:
            print(choice)

        # Prompt the user to enter their answer
        user_answer = input("Enter your answer (a, b, c, or d): ")

        # Evaluate the user's answer
        if user_answer.lower() == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question['answer']}")

        question_counter += 1

    return score


def play_again():
    # Prompt the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"


def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Rules: You will be asked multiple-choice questions. Enter the letter corresponding to your answer.")

    quiz_questions = load_quiz_questions()
    total_questions = len(quiz_questions)

    while True:
        score = present_quiz_questions(quiz_questions)

        final_score = calculate_final_score(score, total_questions)
        display_final_results(final_score)

        if not play_again():
            break


quiz_game()
