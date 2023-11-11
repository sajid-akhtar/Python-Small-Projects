from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# ------------------------- Question Bank -------------------------- #
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# ----------------------------- Creating objects for classes ---------------------------- #
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# ---------------------------- Console print for developers ---------------------------- #
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
