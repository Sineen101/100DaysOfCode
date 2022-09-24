from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI


question_bank = []
for quest in question_data:
    question = quest["question"]
    answer = quest["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)


# while quiz.questions_remaining:
#     quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: <{quiz.score}/{quiz.question_number}>")
