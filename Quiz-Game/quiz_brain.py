class QuizBrain:
    def __init__(self, input_question_list) -> None:
        self.question_number = 0
        self.question_list = input_question_list
        self.score = 0

    def next_question(self):
        user_ans = input(
            f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: ")

        self.check_answer(
            user_ans, self.question_list[self.question_number].answer)

        self.question_number += 1

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("Yoiu got it right!.")
            self.score += 1
        else:
            print("That's wrong!.")
        print(f"The correct answer was: {correct_ans}.")
        print(
            f"Your current score is: {self.score}/{len(self.question_list)}.\n\n")
