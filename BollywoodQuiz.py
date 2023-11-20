from QuestionBollywoodQuiz import Question

# This is a multiple choice quiz about Bollywood

print("Hello!")
print("This is a quiz testing your knowledge on Bollywood movies, actors, and songs. "
      "Let's see how well you will do! There are 10 questions")

# Update questions here
question_prompts = ["What is the most popular genre of Bollywood film?\n(A) Action\n(B) Romance\n(C) Comedy\n",
                    "Which Bollywood actor is known as the \"King of Romance\"?\n(A) SRK\n(B) Salman Khan\n(C) Aamir Khan\n",
                    "Which Bollywood film is considered to be the all-time blockbuster?\n(A) Sholay\n(B) DDLJ\n(C) 3 Idiots\n",
                    "Which Bollywood actress is known as the \"Dancing Queen\"?\n(A) Madhuri Dixit\n(B) Aishwarya Rai Bachchan\n(C) Kareena Kapoor\n",
                    "What is the name of the most popular Bollywood award ceremony?\n(A) Filmfare Awards\n(B) IIFA Awards\n(C) Zee Cine Awards\n",
                    "Which Bollywood film is considered to be a groundbreaking musical?\n(A) Lagaan\n(B) Devdas\n(C) Dil Dhadakne Do\n",
                    "Which Bollywood actress is known for her versatility and strong performances?\n(A) Vidya Balan\n(B) Priyanka Chopra\n(C) Deepika Padukone\n",
                    "What is the name of the most popular Bollywood dance form?\n(A) Kathak\n(B) Bharatanatyam\n(C) Kuchipudi\n",
                    "Which Bollywood film is considered to be a modern classic?\n(A) Rang De Basanti\n(B) Kal Ho Naa Ho\n(C) Chak De! India\n",
                    "Who is considered to be the first superstar of Bollywood?\n(A) Dilip Kumar\n(B) Raj Kapoor\n(C) Rajesh Khanna\n"]
# Update how many questions/answers here
questions = [
    Question(question_prompts[0], "B"),  # 1
    Question(question_prompts[1], "A"),  # 2
    Question(question_prompts[2], "B"),  # 3
    Question(question_prompts[3], "A"),  # 4
    Question(question_prompts[4], "A"),  # 5
    Question(question_prompts[5], "C"),  # 6
    Question(question_prompts[6], "A"),  # 7
    Question(question_prompts[7], "A"),  # 8
    Question(question_prompts[8], "B"),  # 9
    Question(question_prompts[9], "B")  # 10
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        answer = answer.lower()  # Convert user input to lowercase
        correct_answer = question.answer.lower()  # Convert correct answer to lowercase
        if answer == correct_answer:
            score += 1

    # Percentage score
    percentage = (score / len(questions)) * 100
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    print("Grade:", percentage, "%")  # Calculate and print the percentage

    if percentage <= 50:
        print("You got an F on this quiz. Oof. Try harder next time")
    elif percentage <= 60:
        print("Well, you got a D on this quiz. Try again?")
    elif percentage <= 70:
        print("Not bad. You managed to pass with a C.")
    elif percentage <= 80:
        print("Wow! You got a B on this!")
    elif percentage <= 90:
        print("Nice!!! You got an A!")
    elif percentage == 100:
        print("You got all of them correct. Nice job!")


run_test(questions)
