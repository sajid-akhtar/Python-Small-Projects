from turtle import Turtle
import pandas


class StateName (Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.names = []

    def add_state_name(self, name, x, y) -> None:
        new_name = Turtle()
        new_name.hideturtle()
        new_name.penup()
        new_name.goto(x, y)
        new_name.write(name)
        self.names.append(name)

    def generate_csv_of_answers(self) -> None:
        answer = []
        for i in range(len(self.names)):
            answer.append(self.names[i])

        dict_answer = {"State Names": answer}
        data = pandas.DataFrame(dict_answer)
        data.to_csv("D:/Python/python/US-State-Game/answers.csv")
