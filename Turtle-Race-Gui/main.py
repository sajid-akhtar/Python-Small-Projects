from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter the color: ")

colors = ["red", "blue", "green", "purple", "yellow", "cyan"]
position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

is_game_on = False


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True


while is_game_on:
    for tt in all_turtles:
        if tt.xcor() > 220:
            is_game_on = False
            winning_color = tt.pencolor()
            if winning_color == user_bet:
                print(
                    f"You have Won. The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You have Lost. The {winning_color} turtle is the winner!")

        rand_distant = random.randint(0, 10)
        tt.forward(rand_distant)

screen.exitonclick()
