from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        with open("D:/Python/python/Snake-Game-Plain-Gui/data.txt", "r") as file:
            self.high_score = file.read()
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()

    # def game_over(self) -> None:
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT,
    #                font=FONT)

    def reset_board(self) -> None:
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("D:/Python/python/Snake-Game-Plain-Gui/data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
