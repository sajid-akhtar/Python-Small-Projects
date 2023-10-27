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
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT,
                   font=FONT)
