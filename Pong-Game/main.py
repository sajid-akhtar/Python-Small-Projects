from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "a")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision of ball with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # Detect collision of ball with left and right paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_ball_x()

    # Detect if right paddle or left paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
