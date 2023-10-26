from turtle import Screen, Turtle
from snake import Snake
import time

# Screen Controls
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

# Initial 3 Segment Snake
snake = Snake()
screen.update()

# Screen Listening for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
