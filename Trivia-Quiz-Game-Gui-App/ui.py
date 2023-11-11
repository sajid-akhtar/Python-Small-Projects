from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        # Window - Config
        self.window = Tk()
        self.window.title("Quizzler!!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label - Score
        self.score_label = Label(
            text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        # Canvas - Config
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="The text will come here", font=("Arial", 18, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Button - Right
        correct_button_img = PhotoImage(
            file="D:/Python/Python-Small-Projects/Trivia-Quiz-Game-Gui-App/images/true.png")
        self.correct = Button(image=correct_button_img,
                              highlightthickness=0, command=self.true_pressed)
        self.correct.grid(row=2, column=0)

        # Button - Wrong
        incorrect_button_img = PhotoImage(
            file="D:/Python/Python-Small-Projects/Trivia-Quiz-Game-Gui-App/images/false.png")
        self.incorrect = Button(
            image=incorrect_button_img, highlightthickness=0, command=self.false_pressed)
        self.incorrect.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self) -> None:
        '''Function to get the next question from quiz_brain next_question() and update the convas with the question. It also keep check if the quiz is over or not'''
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text=f"You have reached the end of the quiz. Your score: {self.quiz.score}/10")
            self.canvas.config(bg="white")
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")

    def true_pressed(self) -> bool:
        '''Function for correct button press. Returns boolean'''
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self) -> bool:
        '''Function for incorrect button press. Returns boolean'''
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right) -> None:
        '''Function to control canvas background color is the answer selected is right or wrong. Returns none'''
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)
