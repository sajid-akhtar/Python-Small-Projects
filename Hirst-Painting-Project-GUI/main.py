from turtle import Turtle, colormode, Screen
import random

color_list = [(233, 233, 232), (230, 233, 238), (238, 231, 234), (224, 233, 227), (206, 160, 84), (56, 88, 131), (144, 91, 41), (138, 27, 49), (221, 207, 107), (133, 175, 201), (156, 48, 83), (44, 55, 104), (167, 159, 40), (129, 187, 143), (82,
                                                                                                                                                                                                                                                 20, 42), (37, 42, 67), (186, 94, 106), (186, 139, 168), (85, 124, 180), (60, 39, 31), (87, 156, 92), (79, 152, 164), (194, 81, 72), (58, 124, 116), (160, 201, 219), (79, 73, 42), (44, 75, 78), (218, 176, 188), (220, 182, 168), (169, 207, 164)]

colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screenn = Screen()
screenn.exitonclick()
